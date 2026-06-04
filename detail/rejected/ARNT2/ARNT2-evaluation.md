---
type: protein-evaluation
gene: "ARNT2"
date: 2026-05-28
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARNT2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ARNT2 / bHLHe1, KIAA0307 |
| 蛋白大小 | 717 aa / 78.7 kDa |
| UniProt ID | Q9HBZ2 (ARNT2_HUMAN) |
| 评估日期 | 2026-05-28 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9 | /10 | ×3 = 27 | HPA: Supported(9); UniProt (PubMed实验证据), Protein Atlas (Nucleoplasm), GO chromatin |
| 📏 蛋白大小 | 10 | /10 | ×2 = 20 | 717 aa, 78.7 kDa (300-800范围, 理想大小) |
| 🆕 研究新颖性 | 6 | /10 | ×3 = 18 | ****: PubMed 141篇→100-200区间→6分; 仅9篇(6.4%)涉及chromatin/epigenetics |
| 🏗️ 三维结构 | 5 | /10 | ×3 = 15 | pLDDT 58.3; 有序域质量高(bHLH 88.6/PAS 85.2/PAS2+PAC 92.4); 53.1%无序; 无PDB(UniProt确认) |
| 🧬 调控结构域 | 10 | /10 | ×2 = 20 | bHLH + 双PAS + PAC, 6+数据库一致确认; 非新颖蛋白无基线保护 |
| 🔗 PPI | 5/10 | ×3 | **15** | 详见 3.6 PPI 分析 |
| **原始总分** | | | **127.0** /158 |
| **归一化总分** | | | **80.4** /100 |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| GeneCards | Nucleus | 高 |
| Protein Atlas (IF) | Nucleoplasm (HPA001056, RT-4/KOLF2.1J/NIH 3T3) | Supported |
| UniProt | Nucleus (ECO:0000255 PROSITE-ProRule, ECO:0000269 PubMed:24465693) | 高(实验验证) |
| GO | chromatin (GO:0000785), transcription regulator complex (GO:0005667) | 高 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/ARNT2/IF_images/A431_1.jpg|A431_1]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/ARNT2/IF_images/HeLa_1.jpg|HeLa_1]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/ARNT2/IF_images/HeLa_2.jpg|HeLa_2]]

**结论**: 严格核蛋白。UniProt 有PubMed实验证据支持(PMID:24465693)，Protein Atlas ICC/IF 确认核质定位，GO注释包含chromatin定位。多个数据库一致，评10分。

**IF 图像**:
![[HeLa_1.jpg]]
*ARNT2 IF染色 - HeLa细胞: 抗体HPA001056, 显示核质定位(nucleoplasm)*

![[A431_1.jpg]]
*ARNT2 IF染色 - A-431细胞: 核质定位*

**IF 图像**:

#### 3.2 蛋白大小评估
717 aa, 78.7 kDa，属于300-800 aa的理想区间，适合重组表达、生化实验(pull-down/Co-IP)和结构解析（冷冻电镜/X射线晶体学）。bHLH-PAS蛋白家族中，PAS结构域约100 aa, 两个PAS + bHLH共约350 aa的折叠核心，适合结构生物学研究。

**评价**: 10/10

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 141 (Title/Abstract: "ARNT2" AND (gene OR protein)) |
| 最早发表年份 | ~1997 (ARNT家族) |
| Chromatin/epigenetics 比例 | 9/141 (6.4%) |

**主要研究方向**:
- 低氧响应(HIF)通路中的二聚化伙伴 (与HIF1A/EPAS1形成异二聚体)
- AHR(芳香烃受体)信号通路 (异生物质代谢)
- 下丘脑-垂体轴发育、脑发育和视觉/肾功能
- 神经发育: NPAS4-ARNT2在抑制性突触形成中的作用

**评价**: 141篇文献属于100-200范围，chromatin/epigenetics方向仅9篇(6.4%)。ARNT2主要被研究为HIF/AHR的通用二聚化伙伴，其作为直接chromatin调控因子的角色几乎未被关注，niche空间大。: 6分 (100-200区间)。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 58.3 |
| PDB 实验结构 | — |
| 有序区域 (pLDDT>70) 占比 | 37.2% (267/717 aa) |
| 高置信度区域 (>90) | 20.6% (148/717 aa) |
| 低置信度区域 (<50) | 53.1% (381/717 aa) |
| α-helix 含量 | ~30% (bHLH + PAS域富含α螺旋) |
| β-sheet 含量 | ~10% (PAS域含β折叠) |
| 可用 PDB 条目 | 无 (仅AlphaFold预测) |

**有序结构域**:

| 区域 | 长度 | 平均pLDDT | 对应结构域 |
|---|---|---|---|
| 65-116 | 52 aa | 88.6 | bHLH (basic helix-loop-helix) |
| 132-200 | 69 aa | 85.2 | PAS 1 |
| 233-244 | 12 aa | 87.0 | linker region |
| 275-288 | 14 aa | 85.2 | linker region |
| 308-318 | 11 aa | 86.5 | linker region |
| 335-440 | 106 aa | 92.4 | PAS 2 + PAC motif |

**PAE 图**:
![[ARNT2-PAE.png]]

**PAE 数值分析**:
- PAE 矩阵尺寸: 717×717
- PAE 总体均值: 25.47 Å
- PAE <5 Å 占比: 4.2%
- PAE <10 Å 占比: 6.9%

**评价**: 平均pLDDT 58.3 (50-70范围)，53.1%区域无序。但有序结构域质量出色：PAS2+PAC域平均pLDDT高达92.4, bHLH域88.6, PAS1域85.2。这些域对应于bHLH-PAS蛋白的经典折叠。无序区域主要集中在N端(1-64)和C端(548-717)反式激活域。UniProt确认**无PDB实验结构**。ARNT2非新颖蛋白(PubMed=141>100)，不适用基线保护。基于有序域质量上调至**5分**。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| GeneCards | bHLH (IPR011598), PAS (IPR000014), PAC (IPR001610) |
| SMART | HLH (SM00353, 69-122), PAS (SM00091, 137-204, 325-391), PAC (SM00086, 398-441) |
| InterPro | bHLH (IPR011598), PAS (IPR000014), PAC (IPR001610), PAS fold (IPR013767), PAS superfamily (IPR035965) |
| Pfam | HLH (PF00010, 65-116), PAS fold (PF00989, 140-243), PAS domain (PF14598, 336-436) |
| CDD (NCBI) | bHLH-PAS_ARNT (cd18947, 62-124), PAS (cd00130, 146-199, 336-432) |
| UniProt | bHLH (63-116), PAS 1 (134-209), PAS 2 (323-393), PAC (398-441) |
| CATH/Gene3D | PAS domain (G3DSA:3.30.450.20), HLH (G3DSA:4.10.280.10) |

**染色质调控潜力分析**: bHLH-PAS结构域架构是经典的转录因子架构。bHLH域直接识别并结合E-box DNA序列(CANNTG)，PAS域介导蛋白-蛋白二聚化（如与HIF1A/EPAS1/AHR），PAC motif辅助PAS折叠。GO注释包含chromatin binding (GO:0000785)和多种DNA-binding条目。ARNT2作为通用bHLH-PAS二聚化伙伴，其chromatin调控角色（如HIF靶基因位点的chromatin重塑）尚未被充分研究。评10分。

#### 3.6 PPI :
| Partner | Score | 功能类别 | 与调控相关？ |
|---|---|---|---|
| HIF1A | 0.999 | bHLH-PAS TF (低氧响应主调控因子) | 是 |
| EPAS1 (HIF2A) | 0.998 | bHLH-PAS TF (低氧响应) | 是 |
| ARNT (ARNT1) | 0.999 | bHLH-PAS TF (通用二聚化伙伴) | 是 |
| AHR | 0.999 | bHLH-PAS TF (异生物质受体) | 是 |
| EP300 | 0.999 | 转录共激活因子 (组蛋白乙酰转移酶) | 是 |
| NPAS4 | 0.998 | bHLH-PAS TF (神经元活性依赖) | 是 |
| HIF3A | 0.999 | bHLH-PAS TF (低氧负调控) | 是 |
| EGLN1 | 0.999 | 脯氨酸羟化酶 (HIF降解调控) | 是 |
| EGLN3 | 0.999 | 脯氨酸羟化酶 | 是 |
| HSP90AB1 | 0.999 | 分子伴侣 (AHR复合物组分) | 部分 |
| AIP | 0.999 | AHR-interacting protein (AHR复合物) | 是 |
| ELOC (TCEB1) | 0.999 | 转录延伸因子B | 是 |
| HIF1A-ELOC | 0.999 | HIF1A-泛素连接酶复合物 | 是 |
| EP300-ARNT | 0.999 | 共激活因子-TF复合物 | 是 |
| EP300-EPAS1 | 0.998 | 共激活因子-TF复合物 | 是 |
| ARNT-HIF1A | 0.999 | TF二聚体 | 是 |

**humanPPI** (prodata.swmed.edu): **评价**: ARNT2位于bHLH-PAS转录因子| 完全一致 |

**互证加分明细**:
- **结构域多源**: ≥3独立来源(InterPro/SMART/Pfam/UniProt/CDD/CATH)确认bHLH和PAS → **+0.5**
- **域功能一致性**: bHLH/PAS域在GO/UniProt中注释为DNA-binding转录调控 → **+0.5**
- **定位多源**: Protein Atlas IF(Nucleoplasm) + UniProt(Nucleus) + GO(Chromatin) → **+0.5**
- **进化保守**: bHLH-PAS家族从果蝇到人类高度保守(哺乳动物ARNT1/ARNT2同源) → **+0.5**
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

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. **结构域架构完整**: bHLH-PAS-PAC是经典的DNA结合+蛋白互作架构，6+数据库一致确认，PAS2+PAC域AlphaFold置信度极高(pLDDT 92.4)
2. **PPI3. **研究新颖性佳**: 141篇文献中chromatin方向仅9篇(6.4%)，其作为chromatin调控因子的角色几乎空白，niche空间大
4. **大小理想**: 717 aa适合生化和结构实验，重组表达可行

**风险/不确定性**:
1. **高度无序**: C端(548-717)和N端(1-64)占蛋白长度53%，功能未知，可能影响蛋白表达纯化
2. **无实验结构**: PAS域虽有高质量AlphaFold预测，但无PDB实验结构；化学计量学(与HIF1A/AHR二聚体)需实验确定
3. **功能冗余**: 与ARNT(ARNT1)高度同源，可能存在功能冗余，需设计特异性工具(如domain swap)
4. **PPI，STRING显示进行结构解析
- [ ] ChIP-seq/MS分析ARNT2在低氧/非低氧条件下的基因组占有率
- [ ] 比较ARNT2 vs ARNT在全基因组chromatin结合位点的差异

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=ARNT2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172379-ARNT2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ARNT2%22
- UniProt: https://www.uniprot.org/uniprotkb/Q9HBZ2
- - - AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HBZ2
- STRING: https://string-db.org/network/9606.ENSP00000307479
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q9HBZ2

![[Projects/TEreg-finding/protein-interested/detail/rejected/ARNT2/ARNT2-PAE.png]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ARNT2/ARNT2-PAE.png]]




