---
type: protein-evaluation
gene: "ASCL1"
date: 2026-05-28
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ASCL1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ASCL1 / ASH1, HASH1, MASH1, bHLHa46 |
| 蛋白大小 | 236 aa / 25.5 kDa |
| UniProt ID | P50553 (ASCL1_HUMAN) |
| 评估日期 | 2026-05-28 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 10 | /10 | ×3 = 30 | UniProt Nucleus, Protein Atlas Nucleoplasm, GO chromatin binding |
| 📏 蛋白大小 | 8 | /10 | ×2 = 16 | 236 aa, 25.5 kDa (200-300范围) |
| 🆕 研究新颖性 | 2 | /10 | ×3 = 6 | PubMed 598篇, chromatin/epigenetics 157篇(26.3%), 神经发生master regulator极度热门 |
| 🏗️ 三维结构 | 4 | /10 | ×3 = 12 | 平均pLDDT 67.4, bHLH域质量极高(pLDDT 94.0)但N端无序 |
| 🧬 调控结构域 | 10 | /10 | ×2 = 20 | bHLH domain (5+数据库确认), chromatin binding (GO:0003682) |
| 🔗 PPI | 6/10 | ×3 | **18** | 详见 3.6 PPI 分析 |
| ➕ 互证加分 | +2.0 | max +3 | +2.0 | 结构域多源+0.5, 功能一致性+0.5, 定位多源+0.5, 进化保守+0.5 |
| **原始总分** | | | **111.0** /158 |
| **归一化总分** | | | **70.3** /100 |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| GeneCards | Nucleus | 高 |
| Protein Atlas (IF) | Nucleoplasm + Cytosol (HPA076307, SH-SY5Y/HAP1/U2OS) | Supported |
| UniProt | Nucleus | 高 |
| GO | chromatin (GO:0000785), chromatin binding (GO:0003682) | 高 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/ASCL1/IF_images/SH-SY5Y_1.jpg|SH-SY5Y_1]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/ASCL1/IF_images/SH-SY5Y_2.jpg|SH-SY5Y_2]]

**结论**: 主要核定位。Protein Atlas ICC/IF确认Nucleoplasm为主要定位，但有微弱胞质背景(SH-SY5Y中nucleoplasm, U2OS和HAP1中cytosol)。作为bHLH转录因子，核定位是其功能必需的。但胞质信号存在降低了定位的纯度。综合考虑UniProt和GO的一致性，仍评10分。

**IF 图像**:
![[SH-SY5Y_1.jpg]]
*ASCL1 IF染色 - SH-SY5Y细胞: 抗体HPA076307, 显示核质定位(nucleoplasm)*

![[SH-SY5Y_2.jpg]]
*ASCL1 IF染色 - SH-SY5Y细胞: 第二视野*

**IF 图像**:

#### 3.2 蛋白大小评估
236 aa, 25.5 kDa，属于200-300 aa范围。较小的蛋白，bHLH域(118-170, 53 aa)外的N端反式激活域(1-117)部分无序。适合重组表达和生化实验，但相对较小可能限制结构域的多样性。

**评价**: 8/10

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 598 (Title/Abstract: "ASCL1" AND (gene OR protein)) |
| 最早发表年份 | ~1993 (Drosophila achaete-scute complex, 哺乳动物首次克隆) |
| Chromatin/epigenetics 比例 | 157/598 (26.3%) |

**主要研究方向**:
- 神经发生主调控因子: 神经元命运决定、神经分化
- 直接重编程: ASCL1诱导成纤维细胞→神经元
- 小细胞肺癌(SCLC): ASCL1为关键癌基因和谱系存活因子
- 神经发育: 端脑、脊髓、肾上腺嗜铬细胞分化
- 与TCF3/TCF4/TCF12(E蛋白)形成异二聚体调控基因表达

**评价**: 598篇文献属500-2000范围，属于"已被深入研究"区间。chromatin/epigenetics方向157篇(26.3%)，比例相当高。ASCL1是神经生物学领域最知名的转录因子之一，作为直接重编程因子的研究更是近年热点。新切入的niche空间有限，仅可能的chromatin新角度(如pioneer factor activity)尚可探索。评2分。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 67.4 |
| PDB 实验结构 | — |
| 有序区域 (pLDDT>70) 占比 | 32.2% (76/236 aa) |
| 高置信度区域 (>90) | 23.3% (55/236 aa) |
| 低置信度区域 (<50) | 15.3% (36/236 aa) |
| α-helix 含量 | ~25% (bHLH域两个α螺旋) |
| β-sheet 含量 | <5% (基本无) |
| 可用 PDB 条目 | 无 (仅AlphaFold预测) |

**有序结构域**:

| 区域 | 长度 | 平均pLDDT | 对应结构域 |
|---|---|---|---|
| 117-187 | 71 aa | 94.0 | bHLH (basic helix-loop-helix) |

**PAE 图**:
![[ASCL1-PAE.png]]

**PAE 数值分析**:
- PAE 矩阵尺寸: 236×236
- PAE 总体均值: 24.29 Å
- PAE <5 Å 占比: 8.1%
- PAE <10 Å 占比: 12.8%

**评价**: 平均pLDDT 67.4 (50-70范围)。蛋白结构高度两极化：bHLH域(117-187)折叠质量极高(pLDDT 94.0)，显示为典型的helix-loop-helix二聚体化+DNA结合模块。N端(1-116)为反式激活域，大部分无序(pLDDT < 50)。C端(188-236)短小无序。PAE均值高(24.29 Å)，反映bHLH域仅占蛋白约30%。bHLH域的PAE应极低(<5 Å对角线)，而N/C端无序区域拉高了整体PAE。无实验PDB结构。在bHLH蛋白中，bHLH域的高质量预测与其作为DNA结合模块高度匹配。评4分。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| GeneCards | bHLH (IPR011598) |
| SMART | HLH (SM00353, 124-176) |
| InterPro | bHLH (IPR011598, 118-176), Achaete-scute TF family (IPR015660, 61-206) |
| Pfam | HLH (PF00010, 121-171) |
| CDD (NCBI) | bHLH_ASCL1 (cd19742, 115-185) |
| UniProt | bHLH (118-170) |
| CATH/Gene3D | HLH DNA-binding domain (G3DSA:4.10.280.10, 119-181) |

**染色质调控潜力分析**: bHLH结构域是明确的DNA结合转录因子域，直接识别E-box DNA序列(CANNTG)。GO注释包含chromatin binding (GO:0003682)，表明ASCL1直接与chromatin相互作用。作为achaete-scute家族成员，ASCL1的bHLH域与TCF3/TCF4/TCF12(E蛋白)形成异二聚体，后者提供转录激活功能。ASCL1被认为是神经发生过程中的"pioneer"因子，能结合封闭染色质并启始chromatin重塑，这是其chromatin调控角色的高级体现。评10分。

#### 3.6 PPI :
| Partner | Score | 功能类别 | 与调控相关？ |
|---|---|---|---|
| TCF4 | 0.992 | bHLH TF (E蛋白, ASCL1二聚化伙伴) | 是 |
| TCF12 | 0.960 | bHLH TF (E蛋白) | 是 |
| SOX2 | 0.977 | HMG-box TF (干细胞/神经前体) | 是 |
| PAX6 | 0.977 | Paired-box TF (眼/神经发育) | 是 |
| NEUROG2 | 0.976 | bHLH TF (神经元分化) | 是 |
| POU3F2 (BRN2) | 0.971 | POU域TF (神经分化) | 是 |
| MYT1L | 0.964 | 锌指TF (神经元分化) | 是 |
| TCF3 | 0.941 | bHLH TF (E蛋白) | 是 |
| POU3F3 (BRN1) | 0.931 | POU域TF | 是 |
| DLX2 | 0.926 | 同源域TF (中间神经元分化) | 是 |
| ID4 | 0.911 | HLH蛋白 (无DNA结合, 显性负调控) | 是 |
| OLIG1 | 0.959 | bHLH TF (少突胶质细胞) | 是 |
| OLIG2 | 0.952 | bHLH TF | 是 |
| EP300 | 0.941 | 组蛋白乙酰转移酶/共激活因子 | 是 |
| CREB1 | 0.999 | bZIP TF | 是 |

**humanPPI** (prodata.swmed.edu): **评价**: ASCL1的PPI是bHLH二聚化伙伴，SOX2/NEUROG2/PAX6/POU3F2/MYT1L/DLX2都是关键神经转录因子。ID4作为HLH蛋白(无DNA结合域)是竞争性抑制因子。EP300(组蛋白乙酰转移酶)作为共激活因子参与chromatin调控。整个确认bHLH → **+0.5**
- **域功能一致性**: bHLH域在GO中注释为chromatin binding和DNA-binding TF → **+0.5**
- **定位多源**: Protein Atlas IF(Nucleoplasm) + UniProt(Nucleus) + GO(Chromatin) → **+0.5**
- **进化保守**: achaete-scute家族从果蝇到人类高度保守; mouse Ascl1 (Mash1)功能完全保守 → **+0.5**
- 三维结构互证: 无实验PDB → 0
- PPI互证: humanPPI待获取 → 0
**互证总分**: **+2.0** / max +3

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold + PDB | 见 3.4 节 | — |
| 结构域 | UniProt / InterPro / Pfam | 见 3.5 节 | — |
| PPI | STRING | 见 3.6 节 | — |
| 定位 | Protein Atlas IF / UniProt / GO | Nucleus | ✅ |

### 4. 总体评价

**推荐等级**: ★★☆☆☆ (2/5)

**核心优势**:
1. **功能明确且重要**: 神经发生master regulator, pioneer factor活性使其具有独特的chromatin调控机制
2. **bHLH域结构质量极高**: pLDDT 94.0, 显示为典型DNA结合模块
3. **PPI**风险/不确定性**:
1. **极度热门 (致命短板)**: 598篇文献, chromatin方向157篇(26.3%)。作为直接重编程核心因子和神经生物学明星分子, 几乎不可能找到全新的研究角度
2. **蛋白小且无序**: 236 aa中仅bHLH域(53 aa)有结构, N端无序占~50%, 限制了结构生物学方法
3. **无实验结构**: bHLH域虽AlphaFold预测优秀但无PDB, 高分辨率结构解析价值有限(已有bHLH家族多个结构)
4. **竞争激烈**: SCLC、直接重编程、神经发育等领域多个顶级实验室参与

**下一步建议**:
- [ ] **不推荐作为优先研究对象**: 热门度过高(评分仅2), 除非有极其特殊的chromatin角度(如pioneer factor活性依赖的特异性chromatin重塑机制)
- [ ] 如研究, 建议关注ASCL1与其他bHLH TF的功能差异而非蛋白本身

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=ASCL1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139352-ASCL1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ASCL1%22
- UniProt: https://www.uniprot.org/uniprotkb/P50553
- - - AlphaFold: https://alphafold.ebi.ac.uk/entry/P50553
- STRING: https://string-db.org/network/9606.ENSP00000266744
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/P50553

![[Projects/TEreg-finding/protein-interested/detail/rejected/ASCL1/ASCL1-PAE.png]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ASCL1/ASCL1-PAE.png]]




