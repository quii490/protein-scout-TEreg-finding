---
type: protein-evaluation
gene: "AIPL1"
date: 2026-05-28
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AIPL1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | AIPL1 / AIPL2 |
| 蛋白大小 | 384 aa / 43.9 kDa |
| UniProt ID | Q9NZN9 (AIPL1_HUMAN) |
| 评估日期 | 2026-05-28 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×3 | 21.0 | Protein Atlas: mainly nuclear speckles + cytosol (Approved); UniProt: Cytoplasm + Nucleus |
| 📏 蛋白大小 | 10/10 | ×2 | 20.0 | 384 aa，在 300–800 最优范围内 |
| 🆕 研究新颖性 | 8/10 | ×3 | 24.0 | PubMed 175篇，集中于视网膜/LCA研究，chromatin方向完全空白 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21.0 | AlphaFold pLDDT 82.5，76%有序，PAE <5Å占20.8%，折叠质量好 |
| PDB 实验结构 | — |
| 🧬 调控结构域 | 3/10 | ×2 | 6.0 | TPR重复 + FKBP型PPIase域，均为分子伴侣/cochaperone域，非chromatin调控 |
| 🔗 PPI | 0/10 | ×3 | **0** | 详见 3.6 PPI 分析 |
| **原始总分** | | | **95.0/158** | |
| **归一化总分** | | | **60.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Nuclear speckles（主要），Cytosol（额外） | Approved（最高级） |
| GeneCards | Cytoplasm; Nucleus | — |
| UniProt | Cytoplasm, Nucleus | Reviewed (Swiss-Prot) |
| GO | Nucleus, Nucleoplasm, Cytoplasm, Cytosol, Photoreceptor inner segment | — |

**IF 数据**：抗体 HPA026578 在 OE19、U2OS 中显示核斑+胞质信号，U-251MG 仅核质信号。主要定位于核斑（nuclear speckles），附加胞质分布。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/AIPL1/IF_images/U251MG_HPA026578_1.jpg|U251MG_HPA026578_1]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/AIPL1/IF_images/U2OS_HPA026578_1.jpg|U2OS_HPA026578_1]]

**结论**: 蛋白在核与胞质均有分布，主要富集于核斑区域。非严格核蛋白，有一定胞质功能（作为 PDE6 的胞质分子伴侣）。核定位 7 分。

**IF 图像**:

#### 3.2 蛋白大小评估
384 aa，43.9 kDa，处于生化实验和结构解析的最佳范围（300–800 aa）。**评价**: 大小理想，适合重组表达、纯化和结构分析。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 175 |
| 最早发表年份 | ~2000 |
| Chromatin/epigenetics 比例 | ~0%（全部视网膜/LCA方向） |

**主要研究方向**:
- Leber先天性黑曚4型 (LCA4) 致病机制
- 感光细胞特异性 PDE6 分子伴侣功能
- HSP90/HSP70 伴侣异源复合体组分
- FKBP域异戊二烯脂质结合
- TPR域介导的HSP90相互作用
- 视网膜基因替代治疗

**评价**: 175篇文献全部集中于视网膜生物学领域，chromatin/转录调控方向完全空白。如果在此方向有新发现，将是开创性的——但蛋白的已知生物功能（感光细胞特异性cochaperone）使得chromatin调控的发现可能性极低。新颖性 8 分（50–200 范围内，完全未被探索的方向）。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 82.5 |
| 有序区域 (pLDDT>70) 占比 | 76.0% |
| Very high (>90) | 59.4% |
| Confident (70–90) | 16.7% |
| Low (50–70) | 10.9% |
| Very low (<50) | 13.0% |

**高级置信度有序区域**:
- 残基 9–65 (FKBP域, 57 aa)
- 残基 68–111 (FKBP-TPR连接区, 44 aa)
- 残基 131–162 (TPR1, 32 aa)
- 残基 170–328 (TPR2-3 + 部分C端, 159 aa)

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/AIPL1/AIPL1-PAE.png]]

**PAE 数值分析**:
- PAE 矩阵: 384×384, 最大 PAE: 31.75
- 整体均值: 18.97
- PAE <5 Å: 20.8%, PAE <10 Å: 29.2%

**评价**: AlphaFold 预测质量良好（pLDDT 82.5, 76%有序），N端 FKBP域和 C端 TPR域均有高置信度折叠。PAE图显示清晰的对角线低PAE条带（连续二级结构），以及域间中等PAE（域间相对独立）。C端（330–384）无序。整体结构质量 7 分。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | IPR056277: FKBP型PPIase域（N端）；IPR019734: TPR重复；IPR011990: TPR样螺旋超家族；IPR039663: AIP/AIPL1/TTC9家族；IPR046357: PPIase域超家族 |
| UniProt | 无domain注释（comments中domain字段为空） |

**染色质调控潜力分析**: AIPL1 的域架构为典型的分子伴侣/cochaperone：N端 FKBP型 PPIase域负责底物识别（结合异戊二烯化PDE6亚基），C端 TPR域介导HSP90/HSP70招募。两个域均与chromatin/DNA调控无关。这是高度特化的感光细胞伴侣蛋白，在视网膜外几乎所有组织中表达极低。结构域得分 3 分（有域但类型完全不相干，蛋白已被较多研究）。

#### 3.6 PPI :
| Partner | Score | 功能类别 | 与调控相关？ |
|---|---|---|---|
| NUB1 | 0.902 | 泛素样蛋白调控 | 否 |
| AIP | 0.901 | 芳烃受体互作蛋白（分子伴侣） | 否 |
| HSP90AA1 | 0.839 | 分子伴侣 | 否 |
| HSP90AB1 | 0.799 | 分子伴侣 | 否 |
| PTGES3 | 0.794 | 前列腺素E合酶/伴侣 | 否 |
| AHR | 0.885 | 转录因子（通过AIP间接关联） | 间接 |
| RPGRIP1 | 0.731 | 视网膜蛋白 | 否 |

**已知实验验证互作**: NUB1 (Y2H), HSP90 (pull-down), HSP70 (biochemical), PDE6 (functional)

**评价**: 所有高置信度partner均为分子伴侣。AHR 虽为转录因子，但 AIPL1 并非直接与AHR结合——其同源物 AIP 才具有此功能。无任何chromatin remodeling、表观遗传修饰、或DNA结合相关partner。调控相关比例 0/10 = 0%。PPI 得分 1 分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold pLDDT 82.5 | 高置信度折叠，无PDB实验结构比对 | 部分 |
| 结构域 | InterPro / UniProt | InterPro检出FKBP+TPR，UniProt无domain注释 | 部分 |
| PPI | STRING | 全部为伴侣/ UniProt | 一致确认核+胞质双定位 | 一致 ✓ |

**互证加分明细**:
- 定位互证: Protein Atlas (Approved) + UniProt + GO → ≥2来源确认核定位 → **+0.5**
- 其他维度均不满足加分条件

**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**核心优势**:
1. AlphaFold 结构质量好（pLDDT 82.5），76%有序，有清晰折叠域
2. 蛋白大小理想（384 aa），适合生化实验
3. 在 chromatin/转录调控方向完全未被探索（新颖性高）

**风险/不确定性**:
1. **功能不相关**: 这是一个高度特化的感光细胞分子伴侣，其全部已知生物学功能均与视网膜光转导相关，与 TE/chromatin 调控无关
2. **表达限制**: 主要在视网膜感光细胞和松果体中表达，其他组织表达极低
3. **域架构不支持**: FKBP + TPR 是经典伴侣蛋白域架构，缺乏任何 DNA/chromatin 结合潜力
4. **PPI中的非经典功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZN9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129221-AIPL1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AIPL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZN9
- STRING: https://string-db.org/ (API 不可达，数据来自同源物种STRING- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q9NZN9/

![[Projects/TEreg-finding/protein-interested/detail/rejected/AIPL1/AIPL1-PAE.png]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/AIPL1/AIPL1-PAE.png]]




