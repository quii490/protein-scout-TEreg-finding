---
type: protein-evaluation
gene: "N4BP1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## N4BP1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | N4BP1 / — |
| 蛋白名称 | NEDD4-binding protein 1 |
| 蛋白大小 | 896 aa |
| UniProt ID | O75113 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/N4BP1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/N4BP1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | **28** | UniProt Nucleus + 部分胞质 |
| 📏 蛋白大小 | 8/10 | ×1 | **8** | 896 aa，可接受范围 |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 52篇，有一定研究空间 |
| 🏗️ 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 实验结构 + AlphaFold 预测 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 11 个结构域注释，新颖蛋白基线（存在新域发现潜力） |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+2.0** | 核定位: UniProt + GO 双库一致 (+1); 三维结构: AlphaFold + PDB 双源 (+0.5); 结构域: 多库注释一致 (+0.5) |
| **原始总分** |  |  | **117/183** |  |
| **归一化总分** |  |  | **63.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Cytoplasm, cytosol, Nucleus, Nucleus, nucleolus, Nucleus, PML body | 实验/预测 |
| GO Cellular Component | GO:0005634 | N/A |

**结论**: UniProt Nucleus + 部分胞质

#### 3.2 蛋白大小评估

**评价**: 896 aa，896 aa，可接受范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 52 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 6.2602 |

**关键文献**:
1. Kim et al. (2025). "Exogenous RNA surveillance by proton-sensing TRIM25.". *Science*. PMID: 40179174
2. Gitlin et al. (2024). "N4BP1 coordinates ubiquitin-dependent crosstalk within the IκB kinase family to limit Toll-like receptor signaling and inflammation.". *Immunity*. PMID: 38697117
3. Kobayashi et al. (2025). "NEDD4-binding protein 1 suppresses hepatitis B virus replication by regulating viral RNAs.". *J Gen Virol*. PMID: 40111401
4. Zhang et al. (2025). "N4BP1 as a modulator of the NF-κB pathway.". *Cytokine Growth Factor Rev*. PMID: 40312219
5. Gitlin et al. (2020). "Integration of innate immune signalling by caspase-8 cleavage of N4BP1.". *Nature*. PMID: 32971525
**评价**: PubMed 52篇，有一定研究空间

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 896 aa |
| PDB 条目数 | 1 |
| UniProt 注释结构域数 | 11 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/N4BP1/N4BP1-PAE.png]]

**评价**: 1 个 PDB 实验结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | KH_N4BP1_1st |
| InterPro | KH_N4BP1_2nd |
| InterPro | RNase_Zc3h12_NYN |
| InterPro | UBA_N4BP1 |
| InterPro | UBA_N4BP1_C |
| InterPro | ZC3H12/N4BP1_RNase_Reg |
| Pfam | KH_N4BP1_1st |
| Pfam | KH_N4BP1_2nd |
| Pfam | RNase_Zc3h12a |
| Pfam | UBA_N4BP1 |
| Pfam | UBA_N4BP1_C |

**染色质调控潜力分析**: 11 个结构域注释，新颖蛋白基线（存在新域发现潜力）

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| IKBKG | 0 |  | 否 |
| CASP8 | 0 |  | 否 |
| NEDD4 | 0 |  | 否 |
| UBC | 0 |  | 否 |
| ITCH | 0 |  | 否 |
| TRIM25 | 0 |  | 否 |
| ZCCHC2 | 0 |  | 否 |
| RNF19B | 0 |  | 否 |
| ZFAND3 | 0 |  | 否 |
| UBFD1 | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

—

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 11 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 0 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
核定位: UniProt + GO 双库一致 (+1)
三维结构: AlphaFold + PDB 双源 (+0.5)
结构域: 多库注释一致 (+0.5)
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3/5)

**核心优势**:
1. 新颖性: PubMed 52 篇，有一定研究空间
2. 核定位: 明确核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 1 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=N4BP1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102921-N4BP1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22N4BP1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O75113
- STRING: https://string-db.org/network/9606.ENSG00000102921
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75113


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[N4BP1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/N4BP1/N4BP1-PAE.png]]


