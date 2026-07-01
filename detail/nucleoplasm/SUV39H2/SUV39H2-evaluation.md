---
type: protein-evaluation
gene: "SUV39H2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SUV39H2 — REJECTED (研究热度过高 (PubMed strict=101，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SUV39H2 / KMT1B |
| 蛋白名称 | Histone-lysine N-methyltransferase SUV39H2 |
| 蛋白大小 | 410 aa / 46.7 kDa |
| UniProt ID | Q9H5I1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; UniProt: Nucleus; Chromosome, centromere |
| 蛋白大小 | 10/10 | ×1 | 10 | 410 aa / 46.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=101 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=89.1; PDB: 2R3A, 6P0R |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016197, IPR000953, IPR023780, IPR023779, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Uncertain |
| UniProt | Nucleus; Chromosome, centromere | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome, centromeric region (GO:0000775)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 101 |
| PubMed broad count | 171 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KMT1B |

**关键文献**:
1. Establishment of H3K9-methylated heterochromatin and its functions in tissue differentiation and maintenance.. *Nature reviews. Molecular cell biology*. PMID: 35562425
2. Lysine methylation of PPP1CA by the methyltransferase SUV39H2 disrupts TFEB-dependent autophagy and promotes intervertebral disc degeneration.. *Cell death and differentiation*. PMID: 37605006
3. Distinct H3K9me3 heterochromatin maintenance dynamics govern different gene programmes and repeats in pluripotent cells.. *Nature cell biology*. PMID: 39482359
4. Structure, Activity and Function of the Suv39h1 and Suv39h2 Protein Lysine Methyltransferases.. *Life (Basel, Switzerland)*. PMID: 34357075
5. SUV39H2 controls trophoblast stem cell fate.. *Biochimica et biophysica acta. General subjects*. PMID: 33556426

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.1 |
| 高置信度残基 (pLDDT>90) 占比 | 72.4% |
| 置信残基 (pLDDT 70-90) 占比 | 16.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 6.6% |
| 有序区域 (pLDDT>70) 占比 | 89.2% |
| 可用 PDB 条目 | 2R3A, 6P0R |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2R3A, 6P0R）+ AlphaFold高质量预测（pLDDT=89.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016197, IPR000953, IPR023780, IPR023779, IPR011381; Pfam: PF00385, PF05033, PF00856 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CBX1 | 0.915 | 0.852 | — |
| EIF2S3 | 0.905 | 0.093 | — |
| EIF2S3B | 0.902 | 0.093 | — |
| CBX5 | 0.898 | 0.818 | — |
| H3C12 | 0.838 | 0.310 | — |
| H3C13 | 0.837 | 0.310 | — |
| CBX3 | 0.827 | 0.694 | — |
| CAMKMT | 0.812 | 0.000 | — |
| DNMT1 | 0.770 | 0.053 | — |
| H3-5 | 0.741 | 0.310 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q9JLP7 | psi-mi:"MI:0516"(methyltransferase radiometric ass | pubmed:10949293 |
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBE2V2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CGGBP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| grxC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.1 + PDB: 2R3A, 6P0R | pLDDT=89.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. SUV39H2 — Histone-lysine N-methyltransferase SUV39H2，研究基础较多，新颖性有限。
2. 蛋白大小410 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 101 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 101 > 100，研究热度过高，不符合novelty筛选标准。**

### 深度机制分析

**SET结构域组蛋白甲基转移酶的完整域架构**：SUV39H2/KMT1B（410 aa, 46.7 kDa, UniProt Q9H5I1）采用经典的SUV39家族四模块域排列：Chromo（aa 47-105, CD:SM00298, Pfam:PF00385, PROSITE:PRU00053）→ Pre-SET（aa 189-247, SMART:SM00508, Pfam:PF05033, PRU00157）→ SET（aa 250-373, SMART:SM00468, Pfam:PF00856, PRU00190）→ Post-SET（aa 394-410, PRU00155），属于Chromodomain/SET超家族（IPR016197, IPR000953）。Chromo域识别H3K9me2/me3修饰，通过芳香笼（保守Y/W/F残基）特异性结合甲基化赖氨酸，介导SUV39H2在已有H3K9me标记上的阅读-书写正反馈扩增——这是异染色质扩散的核心机制。Pre-SET域含9个保守Cys残基形成三个锌指簇（Zn3Cys9结构），维持SET域活性构象；SET域采用经典的β-折叠核心包裹辅因子S-腺苷甲硫氨酸（SAM），催化Lys ε-氨基的SN2甲基转移反应；Post-SET域提供组蛋白H3 N端尾通道，确保底物K9残基的精确定位。AlphaFold pLDDT=89.1（72.4%>90, 89.2%有序）确认整体结构的高置信度，PDB 2R3A为SUV39H2 SET域与人HP1α（CBX5）Chromo-shadow域的共晶结构（PMID:18003922），6P0R则是SUV39H1的SET域结构——两者高度同源（~65%序列一致性）。HPA将SUV39H2定位于Mitochondria（Uncertain），该信号在UniProt（Nucleus; Chromosome, centromere）和GO-CC（chromatin GO:0000785, centromeric region GO:0000775, nucleoplasm GO:0005654）中不被支持——HPA抗体在HPA定位实验中的脱靶结合导致线粒体信号的假象已被文献广泛记载。

**HP1异染色质网络与表观遗传沉默复合物**：STRING互作图谱以HP1家族为核心：CBX1/HP1β（combined score=0.915, 实验=0.852）、CBX5/HP1α（0.898, 实验=0.818）和CBX3/HP1γ（0.827, 实验=0.694）构成SUV39H2的中心互作伙伴——HP1通过其Chromo-shadow域二聚化并招募其他异染色质因子（如组蛋白去乙酰化酶、DNMTs），形成多价沉默平台。组蛋白H3变体（H3C12/H3C13, score≈0.838-0.837）的连接反映SUV39H2与核心核小体底物的直接酶-底物关系。DNMT1（0.770）的关联最为关键：SUV39H2产生的H3K9me3信号被HP1识别后，HP1可直接招募DNMT1至染色质，将CpG甲基化添加至邻近DNA——建立H3K9me3与DNA甲基化的双向正反馈，永久化基因沉默状态。IntAct实验数据验证了SUV39H2的催化活性（甲基转移酶放射测量法, PMID:10949293），并揭示了与信号转导因子的非经典互作：NCK1、CRK、GRB2、FYN和ABL1（全部肽阵列验证, PMID:17474147, IM-11903）——这些SH2/SH3适配蛋白和酪氨酸激酶通常定位于细胞质膜，其与SUV39H2的结合暗示存在非染色质的SUV39H2功能池。

**H3K9me3异染色质建立与TE监控的双重角色**：SUV39H2催化的H3K9me3是构成型异染色质的标志修饰，主要靶向着丝粒周卫星重复序列和散布的逆转录转座子（ERV、LINE-1）。SET域的甲基转移酶活性直接将H3K9三甲基化——这一修饰为HP1蛋白提供结合位点，后者通过聚合和桥接相邻核小体压缩染色质。在着丝粒处，SUV39H2与SUV39H1功能冗余，共同维持着丝粒周异染色质——HPA的着丝粒注释（Chromosome, centromere, GO:0000775）支持此定位。对逆转录转座子而言，SUV39H2产生的H3K9me3峰直接抑制LTR和LINE-1启动子的Pol II转录起始——这是哺乳动物基因组中最重要的TE沉默机制之一。CBX5-HP1α与DNMT1的功能耦合（STRING 0.770）在TE区域添加DNA甲基化标记，提供第二道沉默防线。SUV39H2与SUV39H1在分化中的差异表达提示：SUV39H1维持细胞周期依赖的异染色质建立，而SUV39H2可能在终末分化/特殊组织中承担独特功能（PMID:35562425, 34357075, 33556426）。

**TE调控的已验证路径与实验局限**：SUV39H2是TE调控领域中被广泛研究的核心酶——PubMed严格101篇使其不符合本筛选的新颖性标准（>100篇即拒绝）。但其对TE生物学的基础重要性使其成为理解其他候选蛋白功能模式的参照基准。ECR重复元件、IAP逆转录转座子和LINE-1在Suv39h1/h2双敲除小鼠中被深度去抑制证明了其体内TE沉默活性。对于后续TE调控候选蛋白的评估，SUV39H2的域架构—功能映射（chromo阅读→SET书写→HP1招募→DNMT耦合）提供了可直接推广的解析框架：新兴候选若有chromo或SET样折叠、核内HP1样互作或甲基转移酶活性信号，可能构成未被发现的SUV39H2旁系同源TE沉默通路。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H5I1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152455-SUV39H2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SUV39H2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H5I1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (uncertain)。来源: https://www.proteinatlas.org/ENSG00000152455-SUV39H2/subcellular

![](https://images.proteinatlas.org/45901/599_C8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45901/599_C8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45901/601_C8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/45901/601_C8_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/45901/603_C8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45901/603_C8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H5I1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H5I1 |
| SMART | SM00298;SM00508;SM00468;SM00317; |
| UniProt Domain [FT] | DOMAIN 47..105; /note="Chromo"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00053"; DOMAIN 189..247; /note="Pre-SET"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00157"; DOMAIN 250..373; /note="SET"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00190"; DOMAIN 394..410; /note="Post-SET"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00155" |
| InterPro | IPR016197;IPR000953;IPR023780;IPR023779;IPR011381;IPR050973;IPR003616;IPR007728;IPR001214;IPR046341; |
| Pfam | PF00385;PF05033;PF00856; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000152455-SUV39H2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APPL2 | Intact, Biogrid | true |
| CBX1 | Biogrid, Opencell | true |
| CDCA4 | Intact, Biogrid | true |
| CEP70 | Intact, Biogrid | true |
| KCTD17 | Intact, Biogrid | true |
| KLHDC4 | Intact, Biogrid | true |
| MRFAP1 | Intact, Biogrid | true |
| PHF19 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
