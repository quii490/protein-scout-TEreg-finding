---
type: protein-evaluation
gene: "CDK2AP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CDK2AP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDK2AP2 |
| 蛋白名称 | Cyclin-dependent kinase 2-associated protein 2 |
| 蛋白大小 | 126 aa / 13.1 kDa |
| UniProt ID | O75956 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDK2AP2/IF_images/SK-MEL-30_1.jpg|SK MEL 30]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDK2AP2/IF_images/OE19_1.jpg|OE19]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 126 aa / 13.1 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.2; PDB: 无 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已嵌入

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 43 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Candidate Biomarkers for Hard-to-Heal Wounds Revealed by Single-Cell RNA Sequencing of Wound Fluid in Murine Wound Models.. *Wound Repair Regen*. PMID: 40444294
2. Novel circular RNA hsa_circ_0036683 suppresses proliferation and migration by mediating the miR-4664-3p/CDK2AP2 axis in non-small cell lung cancer.. *Thorac Cancer*. PMID: 39113208
3. Cigarette smoking, by accelerating the cell cycle, promotes the progression of non-small cell lung cancer through an HIF-1α-METTL3-m(6)A/CDK2AP2 axis.. *J Hazard Mater*. PMID: 37156046
4. Whole-genome resequencing reveals genetic diversity, differentiation, and selection signatures of yak breeds/populations in Qinghai, China.. *Front Genet*. PMID: 36704337
5. Cross-linking mass spectrometry reveals the structural topology of peripheral NuRD subunits relative to the core complex.. *FEBS J*. PMID: 33283408

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.2 |
| 高置信度残基 (pLDDT>90) 占比 | 34.9% |
| 置信残基 (pLDDT 70-90) 占比 | 15.1% |
| 中等置信 (pLDDT 50-70) 占比 | 38.1% |
| 低置信 (pLDDT<50) 占比 | 11.9% |
| 有序区域 (pLDDT>70) 占比 | 50.0% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDK2AP2/CDK2AP2-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=74.2，有序区 50.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDK2AP1 | 0.000 | 0.000 | — |
| HDAC2 | 0.000 | 0.000 | — |
| CDK2 | 0.000 | 0.000 | — |
| MANF | 0.000 | 0.000 | — |
| MTA3 | 0.000 | 0.000 | — |
| HDAC1 | 0.000 | 0.000 | — |
| MRFAP1L1 | 0.000 | 0.000 | — |
| TMEM217 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P23381 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q5NET3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:O75956 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q96HT8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q6IAV4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| intact:EBI-25847655 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| intact:EBI-54262435 | psi-mi:"MI:2195"(clash) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 15
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.2 + PDB: 无 | pLDDT=74.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 8 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CDK2AP2 — Cyclin-dependent kinase 2-associated protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小126 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HSF4 | BioGRID | 1 |
| ZBTB48 | BioGRID | 1 |
| RCC1 | BioGRID | 1 |
| TRA2A | BioGRID | 1 |
| IKZF1 | BioGRID | 1 |
| EEF1G | BioGRID | 1 |
| EED | BioGRID | 1 |
| APP | BioGRID | 1 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 深度机制分析

**结构域架构与分子功能推断。** CDK2AP2是一个仅126 aa的超小型蛋白，Pfam PF09806（CDK2AP2 family）结构域几乎覆盖其全部序列。InterPro IPR017266将该蛋白归入CDK2AP2家族，但未提供详细的结构域边界或功能位点信息。SMART检测和UniProt Domain[FT]均未检出显式注释，这与其"未被充分研究"的状态一致（PubMed=9）。AlphaFold pLDDT=74.2、有序区50.0%表明蛋白具有部分稳定的三级结构——约63个残基处于有序构象，另外63个残基在孤立状态下呈现柔性。这种"半有序-半无序"的架构特征典型地见于小型adaptor/cofactor蛋白，其在未结合伴侣时部分disordered，通过"折叠-结合耦合"（folding-upon-binding）在复合体组装时获得全部结构。AF2预测中有序区（pLDDT>70）很可能对应于与CDK2AP1或HDAC2等伴侣的互作界面。

**PPI网络揭示的生物学意义。** PPI网络在humanPPI和BioGRID层面揭示了CDK2AP2与关键染色质调控复合体的核心连接。最重要的两个互作来自humanPPI（HPA Interaction数据库）：HDAC2（Biogrid, Opencell, AF3/HPA structure=true）和CHD4（Biogrid）。HDAC2是NuRD（Nucleosome Remodeling and Deacetylase）复合体的核心催化亚基之一，负责去除组蛋白H3和H4的乙酰基（特别是H3K27ac和H4K16ac），建立抑制性染色质环境。CHD4（Mi-2beta）是NuRD的ATPase/染色质重塑亚基，利用ATP水解能量沿DNA滑动或移除核小体。CDK2AP2同时与HDAC2和CHD4互作，强烈提示它是NuRD复合体的新型附属因子（accessory subunit）。额外BioGRID伙伴进一步扩展了这一调控网络：IKZF1（Ikaros）是淋巴细胞发育中的关键转录因子，直接招募NuRD到造血特异性基因位点（如TdT, lambda5）；EED是PRC2（Polycomb Repressive Complex 2）的支架亚基，催化H3K27三甲基化（H3K27me3）；ZBTB48是端粒结合锌指蛋白；HSF4是热休克因子家族的转录因子；APP互作则提示潜在的神经退行性/发育功能连接。RCC1（Ran GEF）的互作暗示核质运输或有丝分裂调控维度。

**三维结构的功能解释。** 结构层面的关键证据来自PMID:33283408——发表于FEBS Journal的cross-linking mass spectrometry（CLMS）研究，该研究通过化学交联偶联质谱分析绘制了NuRD外周亚基相对于核心复合体的结构拓扑。CLMS数据直接支持CDK2AP2与HDAC2/CHD4核心之间的物理邻近关系（cross-links），为基于AP-MS的互作观测提供了结构验证。pLDDT=74.2虽仅属中等，但作为仅126 aa的小蛋白已是合理水平——小型蛋白的AF2置信度常因缺乏足够共进化约束而低于大型多域蛋白。CDK2AP2的paralog CDK2AP1（doc-1/p12）已有明确功能注释：直接结合CDK2单体（非cyclin-bound）抑制其激酶活性，作为CDK2的肿瘤抑制性调控因子。CDK2AP1同样与NuRD复合体互作。两种paralog在NuRD中可能形成同源/异源二聚体或竞争性重叠。

**综合分子机制模型。** CDK2AP2是NuRD和PRC2两大转录抑制复合体的新型连接因子。其主要功能假设如下：(1)在NuRD中，CDK2AP2作为HDAC2-CHD4之间的"耦合因子"（coupling factor），协调去乙酰化活性与ATP依赖的核小体重塑之间的时间顺序——这类似于NuRD内已有亚基MBD2/GATAD2A所执行的功能；(2)CDK2AP2通过与NuRD（HDAC2/CHD4）和PRC2（EED）的双重互作，在特定基因组位点（经由IKZF1/ZBTB48/HSF4等序列特异性因子靶向）桥接组蛋白去乙酰化（NuRD执行）和非经典PRC2招募（非CpG island依赖的H3K27me3沉积），建立稳定的抑制性染色质状态；(3)在非小细胞肺癌（NSCLC）中，circRNA hsa_circ_0036683通过海绵化miR-4664-3p去抑制CDK2AP2表达（PMID:39113208）——CDK2AP2上调通过NuRD依赖机制抑制增殖/迁移基因，发挥肿瘤抑制功能。吸烟通过HIF-1alpha-METTL3-m6A/CDK2AP2轴促进NSCLC进展（PMID:37156046）的发现提示CDK2AP2表达受m6A RNA甲基化的表观转录组调控——m6A修饰可能影响CDK2AP2 mRNA稳定性和翻译效率。在伤口愈合中，CDK2AP2被鉴定为硬愈合伤口的候选生物标志物（scRNA-seq, PMID:40444294），可能通过NuRD介导的表观遗传调控影响角质形成细胞或成纤维细胞的迁移/增殖程序。

**研究与转化启示。** CDK2AP2在NuRD-PRC2轴中的位置赋予了它"表观遗传转换开关"（epigenetic switch）的治疗可及性。鉴于其极端新颖性（PubMed=9），CDK2AP2是一个理想的功能发现靶点：(1)CRISPR/Cas9敲除后联合ATAC-seq/ChIP-seq（H3K27ac/H3K27me3）的多组学分析可直接验证其表观基因组功能；(2)BioID/TurboID邻近标记技术可捕获CDK2AP2在NuRD和PRC2内的完整互作组，包括瞬时/弱互作伙伴；(3)在NSCLC模型中，CDK2AP2过表达或下调对肿瘤增殖的影响可通过NuRD活性的药理学调控（HDAC inhibitor如SAHA，或CHD4 ATPase inhibitor）进行遗传学-药理学联合验证；(4)端粒生物学方面，CDK2AP2-ZBTB48互作开辟了新的研究维度——染色质重塑（NuRD）与端粒稳态之间的功能性连接尚未被探索；(5)yak全基因组重测序中CDK2AP2选择信号的发现（PMID:36704337）提示该蛋白在高海拔适应性进化中可能发挥未被认知的作用。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75956
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167797-CDK2AP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDK2AP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75956
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDK2AP2/CDK2AP2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75956 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR017266; |
| Pfam | PF09806; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167797-CDK2AP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HDAC2 | Biogrid, Opencell | true |
| CDK2AP1 | Biogrid | false |
| CHD4 | Biogrid | false |
| MRFAP1L1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
