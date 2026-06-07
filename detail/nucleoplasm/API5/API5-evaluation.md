---
type: protein-evaluation
gene: "API5"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation, ]
status: scored
---

## API5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | API5 / AAC-11, FIF, MIG8, XAGL |
| 蛋白大小 | 524 aa / ~59.4 kDa |
| UniProt ID | Q9BZZ5 (API5_HUMAN) |
| 评估日期 | 2026-05-28 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/API5/IF_images/212_C4_1_red_green.jpg|212_C4_1_red_green]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/API5/IF_images/212_C4_2_red_green.jpg|212_C4_2_red_green]]

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | **32** | nuclear speckles; UniProt: mainly nuclear; NLS 454-475 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 524 aa / 59.4 kDa, 理想实验范围 |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 63篇; 50-200范围; chromatin方向空白大 |
| 🏗️ 三维结构 | 10/10 | ×3 | **30** | PDB: 3U0R(2.50A)/3V6A(2.60A)/6L4O(2.60A全链) X-ray; AF pLDDT 84.6; PDB+AF双重验证→10 |
| 🧬 调控结构域 | 6/10 | ×2 | **12** | ARM/HEAT repeats(蛋白互作域); 新颖基线6 |
| 🔗 PPI | 4/10 | ×3 | **12** | 凋亡(ACIN1)+FGF2+RNA加工(DDX39B)为主; 0% chromatin partner |
| ➕ 互证加分 | — | — | **+2.0** | PDB+AF吻合+fold一致; >=3源结构域; >=2源定位; 进化保守 |
|  | **原始总分** |  | **148/183** | **128.0/183** |  |
|  | **归一化总分** |  | **80.9/100** | **69.9/100** |  |

#### 3.6 PPI 网络（四源综合）

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| PRKAB1 | anti bait coimmunoprecipitation | 17353931 | AMPK subunit, energy sensor | ❌ |
| SOCS6 | cross-linking study | 30021884 | Cytokine signaling suppressor | ❌ |
| LTV1 | cross-linking study | 30021884 | Ribosome biogenesis | ❌ |
| OSGEPL1 | cross-linking study | 30021884 | tRNA threonylcarbamoyladenosine | ❌ |
| FRG2 | cross-linking study | 30021884 | FSHD region gene | ❌ |
| CEP112 | cross-linking study | 30021884 | Centrosomal protein | ❌ |
| HILS1 | cross-linking study | 30021884 | Histone H1-like, spermatid-specific | ✅ |
| BICDL2 | validated two hybrid | 32296183 | Motor protein adaptor | ❌ |
| HTT | two hybrid | 17500595 | Huntingtin, transcriptional regulation | ✅ |
| ATXN10 | two hybrid array | 32814053 | Ataxin-10 | ❌ |
| NDUFV2 | two hybrid pooling approach | 32814053 | Mitochondrial Complex I | ❌ |
| DDX39B | cross-linking study | 30021884 | mRNA export helicase (TREX complex) | ❌ |

**STRING 预测互作** (已知功能方向):
- ACIN1 (apoptotic chromatin condensation), FGF2 (growth factor), DDX39B (TREX mRNA export)
- 主要集中于凋亡调控、RNA加工和生长因子信号通路

**已知复合体成员** (GO Cellular Component):
- Nuclear speck (GO:0016607) — 剪接/RNA加工核内枢纽
- Spliceosomal complex (GO:0005681)
- Nucleus, Cytoplasm, Membrane

**PPI 互证分析**:
- 调控相关比例: 2/12 (16.7%) — HILS1 (组蛋白H1样蛋白), HTT (亨廷顿蛋白/转录调控)
- IntAct 实验互作以细胞质/代谢蛋白为主（PRKAB1, NDUFV2）和交联质谱捕获的核蛋白
- Nuclear speck + spliceosomal complex GO 注释与 RNA processing 功能方向一致，非经典染色质调控

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/API5/API5-PAE.png]]

**评价**: API5 的 PPI 网络未呈现明显的染色质/转录调控富集。IntAct 实验互作以代谢和信号蛋白为主。HILS1（组蛋白H1样睾丸特异蛋白）的交联研究互作可能为间接关联。HTT（亨廷顿蛋白）虽涉及转录调控但为神经退行性疾病蛋白。Nuclear speck 和 spliceosomal complex 的 GO-CC 注释确认 API5 位于 RNA 加工相关亚核结构，但此定位与剪接/mRNA 代谢更相关，而非直接染色质调控。PPI 评分维持 4（调控比例 ~17%）。

### X. 关键文献 (PubMed)

1. Sharma VK et al. (2021). "Interplay between p300 and HDAC1 regulate acetylation and stability of Api5 to regulate cell proliferation.". *Sci Rep*. PMID: 34385547
2. Bong SM et al. (2020). "Regulation of mRNA export through API5 and nuclear FGF2 interaction.". *Nucleic Acids Res*. PMID: 32383752
3. Garcia-Jove Navarro M et al. (2013). "Api5 contributes to E2F1 control of the G1/S cell cycle phase transition.". *PLoS One*. PMID: 23940755
4. Kuttanamkuzhi A et al. (2023). "Altered expression of anti-apoptotic protein Api5 affects breast tumorigenesis.". *BMC Cancer*. PMID: 37095445
5. Morris EJ et al. (2006). "Functional identification of Api5 as a suppressor of E2F-dependent apoptosis in vivo.". *PLoS Genet*. PMID: 17112319

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 蛋白大小理想 (524 aa)，结构质量优异 (pLDDT 84.6)
2. 研究新颖性高 (63篇)，chromatin 方向几近空白
3. Nuclear speckles 定位提示可能与 RNA 加工/转录调控交叉
4. 高置信度 ARM/HEAT 折叠域可能具有未发现的核酸结合功能

**风险/不确定性**:
1. 无任何已知 chromatin/DNA 结合结构域，功能推断缺乏结构基础
2. 已知 PPI 系统鉴定 API5 的核内互作组
- [ ] 利用 ChIP-seq / CUT&RUN 检测 API5 是否与染色质结合
- [ ] 分析 nuclear speckles 定位是否参与 transcription-coupled RNA processing
- [ ] AlphaFold 折叠域与已知核酸结合域做三维结构比对，寻找潜在 homology

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BZZ5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=API5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BZZ5
- InterPro: https://www.ebi.ac.uk/interpro/protein/Q9BZZ5/
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166181-API5
- STRING: (API 不可达)
- humanPPI: 


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[API5-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/API5/API5-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BZZ5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008383;IPR011989;IPR016024; |
| Pfam | PF05918; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166181-API5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DDX39B | Intact, Biogrid, Opencell | true |
| ACIN1 | Intact, Biogrid | false |
| CDC5L | Biogrid | false |
| CPSF6 | Opencell | false |
| DDX27 | Biogrid | false |
| DDX39A | Biogrid | false |
| EBNA1BP2 | Biogrid | false |
| HNRNPK | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
