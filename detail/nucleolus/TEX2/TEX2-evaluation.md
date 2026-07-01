---
type: protein-evaluation
gene: "TEX2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TEX2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TEX2 / HT008|TMEM96|KIAA1738 |
| 蛋白全称 | Testis-expressed protein 2 |
| 蛋白大小 | 1127 aa |
| UniProt ID | Q8IWB9 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TEX2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TEX2/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | **24** | 细胞核+细胞质，UniProt 支持核定位 |
| 蛋白大小 | 8/10 | ×1 | **8** | 1127 aa，尚可接受 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 14 篇，极度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 2 domain(s), 新颖蛋白基线水平 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.0** | None |
| **原始总分** |  |  | **120/183** |  |
| **归一化总分** |  |  | **65.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Endoplasmic reticulum membrane, Nucleus membrane | 实验证据/预测 |
| GO-CC | GO:0005634 | IEA |

**结论**: 细胞核+细胞质，UniProt 支持核定位

#### 3.2 蛋白大小评估

**评价**: 1127 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 14 |

**评价**: PubMed 14 篇，极度新颖

**关键文献**:
1. Wang R & Dobritsa AA (2021). "Loss of THIN EXINE2 disrupts multiple processes in the mechanism of pollen exine formation". *Plant Physiol*. PMID: 34618131
2. Sieper MH et al. (2024). "Scrutinizing the human TEX genes in the context of human male infertility". *Andrology*. PMID: 37594251
3. Hu X et al. (2024). "Recent Advances on Synaptotagmin-Like Mitochondrial-Lipid Binding Protein Domain Containing Lipid Transfer Proteins". *Contact (Thousand Oaks)*. PMID: 39139576
4. Du Y et al. (2023). "Tex2 is required for lysosomal functions at TMEM55-dependent ER membrane contact sites". *J Cell Biol*. PMID: 36705603
5. Carqueijeiro I et al. (2018). "Two Tabersonine 6,7-Epoxidases Initiate Lochnericine-Derived Alkaloid Biosynthesis in Catharanthus roseus". *Plant Physiol*. PMID: 29934299
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 1127 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 2 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TEX2/TEX2-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | SMP_LBD |
| PROSITE | SMP |

**染色质调控潜力分析**: 2 domain(s), 新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| ezrA | two hybrid pooling approach | 20711500 | — | — |
| a0a5p8ycv0_yerpe | two hybrid pooling approach | 20711500 | — | — |
| hsamir4235p | clash | 23622248 | — | — |
| ECE1 | two hybrid | 38413612 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

--

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 2 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
--
**总计**: +0.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 14 篇，极度新颖
2. 核定位: 部分核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | BioGRID | 0 |
| DYNLT1 | BioGRID | 0 |
| TMEM216 | BioGRID | 0 |
| SLC6A15 | BioGRID | 0 |
| MRAP2 | BioGRID | 0 |
| EFNB2 | BioGRID | 0 |
| TRIM25 | BioGRID | 0 |
| CANX | BioGRID | 0 |


### 深度机制分析

**SMP-LTD脂质转移域的膜接触位点架构**：TEX2（1127 aa, Q8IWB9）是哺乳动物Synaptotagmin-like Mitochondrial-lipid binding Protein（SMP）家族成员，其核心结构域为单拷贝SMP-LTD（Lipid Transfer Domain, IPR031468, PROSITE:PRU01194, UniProt FT: DOMAIN 816-1101），采用管状疏水腔折叠——长约20-25 Å的β-sandwich腔道可容纳单分子磷脂穿梭于供体和受体膜之间。SMP域在进化上属于TULIP超家族（管状脂质结合蛋白），其脂质转移活性不依赖ATP或膜融合——仅通过浓度梯度驱动的被动扩散在两种膜之间运送甘油磷脂和鞘脂。TEX2的1127 aa尺寸中，SMP域仅占约286 aa（816-1101），暗示N端约800 aa区域含非催化结构域——可能介导亚细胞定位、膜锚定或蛋白互作。

**内质网-溶酶体MCS与核膜外脂质稳态**：UniProt注释TEX2定位于Endoplasmic reticulum membrane和Nucleus membrane，GO-CC亦含endoplasmic reticulum membrane。Du等人（2023, PMID:36705603）的功能研究揭示TEX2在TMEM55依赖的ER-溶酶体膜接触位点（MCS）上发挥功能——TMEM55为溶酶体PI(4,5)P2 4-磷酸酶，其催化产生的PI(4)P被TEX2识别并促进ER向溶酶体的脂质转移。HumanPPI互作数据进一步确认ER定位：VAPA（VAMP-associated protein A, Biogrid/Opencell）是标志性ER MCS系留蛋白，通过FFAT基序识别含SMP域的脂质转移蛋白；RTN4（reticulon 4, Biogrid/Opencell）和BCAP31（B-cell receptor-associated protein 31, Biogrid）均属ER膜蛋白，参与ER形态维持和蛋白转运。NUP155（核孔蛋白155 kDa, Biogrid互作）和EMD（emerin, Biogrid互作）则直接指向内核膜——NUP155是核孔复合物Y-complex的亚基，EMD是内核膜LEM域蛋白，两者共同参与核膜结构和核-质运输。

**核膜定位与TE调控的间接可能**：TEX2的HPA IF重新定位（HPA IF 图像修正块）确认为Nucleoplasm（Approved）——这与UniProt的"Nucleus membrane"注释结合暗示TEX2可能在内核膜处执行脂质转移功能，但也可能在核质中（以不依赖膜的可溶性形式）发挥替代功能。若TEX2确实定位于内核膜，其脂质转移活性可能影响核膜的脂质组成和流动性——继而通过改变核膜相关异染色质（LADs, lamina-associated domains）的物理性质间接影响TE沉默。LADs富集LINE-1和LTR元件，其转录沉默依赖于核膜lamina蛋白（lamin A/C, lamin B1）和EMD——TEX2-EMD互作（Biogrid）暗示TEX2可能与EMD/LEM-Domains-含蛋白的核膜染色质锚定功能耦合。

**实验前景与PPI数据的空洞**：极度新颖（PubMed=14篇, 50/50分）、明确核膜/核质定位和SMP脂质转移的确定生化功能使TEX2成为有吸引力的跨学科候选。然而，PPI数据极为稀少（6/30分）——STRING互作列表为空，humanPPI仅有Biogrid互作（全部score=0），表明TEX2在标准高通量PPI方法（酵母双杂交、AP-MS）中系统性失检。这可能因为TEX2是整合膜蛋白（含跨膜螺旋，UniProt标注"Endoplasmic reticulum membrane"），而整合膜蛋白在标准PPI方法的裂解条件下倾向于聚集和沉淀。实验优先级：（1）TEX2-NUP155和TEX2-EMD的co-IP验证其核膜定位；（2）体外脂质转移实验确定TEX2 SMP域对PI(4)P和其他磷脂的底物选择性；（3）TEX2敲除后核膜脂质组学分析；（4）若核膜脂质变化，检测LAD区TE去抑制。归一化得分65.6/100，鉴于TEX2的极端新颖性和独特功能域，可作为跨学科TE-膜脂信号的双功能探索靶标。

### TE 调控评估

该蛋白具有核定位证据，可能间接参与核内 TE 调控过程，但目前无直接实验证据支持。需实验验证。

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TEX2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136478-TEX2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TEX2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q8IWB9
- STRING: https://string-db.org/network/9606.ENSG00000136478
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IWB9


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 暂无互作数据 |

暂无实验验证互作。无 BioGrid 补充数据。

![[TEX2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/TEX2/TEX2-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000136478-TEX2/subcellular

![](https://images.proteinatlas.org/57116/942_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/57116/942_H7_3_red_green.jpg)
![](https://images.proteinatlas.org/57116/955_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/57116/955_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/57116/972_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/57116/972_H7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IWB9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 816..1101; /note="SMP-LTD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01194" |
| InterPro | IPR031468; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000136478-TEX2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| COPE | Biogrid, Opencell | true |
| RTN4 | Biogrid, Opencell | true |
| VAPA | Biogrid, Opencell | true |
| BCAP31 | Biogrid | false |
| CKAP4 | Biogrid | false |
| EMD | Biogrid | false |
| FKBP8 | Biogrid | false |
| NUP155 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
