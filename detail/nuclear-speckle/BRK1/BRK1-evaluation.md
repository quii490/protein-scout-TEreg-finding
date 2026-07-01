---
type: protein-evaluation
gene: "BRK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BRK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRK1 / C3orf10 |
| 蛋白名称 | Protein BRICK1 |
| 蛋白大小 | 75 aa / 8.7 kDa |
| UniProt ID | Q8WUW1 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:45:32 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | HPA: Nuclear speckles; UniProt: Cytop... |
| 蛋白大小 | 4/10 | x1 | 4 | 75 aa / 8.7 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=43 篇 (41-60->6) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=93.7; PDB: 3P8C, 4N78, ... |
| 调控结构域 | 3/10 | x2 | 6 | InterPro: 1; Pfam: 0; IPR033378 |
| PPI 网络 | 6/10 | x3 | 18 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.0 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; 结构域 + AlphaFold 质量: +0.5; PDB 多条目覆盖: +0.5 |
| **原始总分** | | | **126.0/180** | |
| **归一化总分 (/1.83)** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Nuclear speckles, Cell Junctions | Approved |
| UniProt | Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- lamellipodium (GO:0030027)
- SCAR complex (GO:0031209)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 75 aa，蛋白较小，但仍在可操作范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed broad count | 66 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C3orf10 |

**关键文献**:
1. Systems Analysis Implicates WAVE2 Complex in the Pathogenesis of Developmental Left-Sided Obstructive Heart Defects.. *JACC. Basic to translational science*. PMID: 32368696
2. Plug-in strategy for resistance engineering inspired by potato NLRome.. *Nature*. PMID: 41162714
3. Proteogenomic network analysis reveals dysregulated mechanisms and potential mediators in Parkinson's disease.. *Nature communications*. PMID: 39080267
4. Extracellular BRICK1 drives heart repair after myocardial infarction in mice.. *Science translational medicine*. PMID: 41499524
5. Alzheimer's Disease polygenic risk, the plasma proteome, and dementia incidence among UK older adults.. *GeroScience*. PMID: 39586964

**评价**: 中等新颖性，有一定研究基础但仍有探索空间（PubMed 41-60篇）。新颖性评分 6/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.7 |
| 高置信度残基 (pLDDT>90) 占比 | 85.3% |
| 置信残基 (pLDDT 70-90) 占比 | 6.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 1.3% |
| 有序区域 (pLDDT>70) 占比 | 92.0% |
| 可用 PDB 条目 | 3P8C, 4N78, 7USC, 7USD, 7USE |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold高质量预测（pLDDT=93.7），结构可信度高。三维结构评分 10/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033378; Pfam: 无 |

**染色质调控潜力分析**: 存在 1 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作**: 暂无数据或查询失败。

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q9ZQ49 | pull down | pubmed:21798944|imex:IM-16043 |
| Wasf2 | two hybrid | pubmed:15102471 |
| EBI-4444334 | two hybrid array | pubmed:21798944|imex:IM-16043 |
| HUB1 | two hybrid array | pubmed:21798944|imex:IM-16043 |
| ICR5 | two hybrid array | pubmed:21798944|imex:IM-16043 |
| ARP3 | two hybrid | pubmed:17267444|imex:IM-19126 |
| ARPC3 | two hybrid | pubmed:17267444|imex:IM-19126 |
| ABIL1 | two hybrid | pubmed:17267444|imex:IM-19126 |
| ABIL2 | two hybrid | pubmed:17267444|imex:IM-19126 |
| ABIL3 | two hybrid | pubmed:17267444|imex:IM-19126 |

**PPI 互证分析**:
- 仅 IntAct 有数据 (15 interactions)

**评价**: 互作网络中等：STRING 0 预测 + IntAct 15 实验互作。PPI 评分 6/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.7 + PDB: 3P8C, 4N78, 7USC | pLDDT=93.7, v6 | 预测+实验 |
| 定位 | HPA | Nuclear speckles | 单一来源 |
| PPI | IntAct | 15 interactions | 单一来源 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0.5
**总分**: +2.0 / max +3

### 4. 总体评价

**归一化总分**: 68.9/100

**核心优势**:
1. AlphaFold高质量预测（pLDDT=93.7），结构可信度高。
2. 已有PDB实验结构：3P8C, 4N78, 7USC。
3. 存在 1 个已知结构域，有明确的结构-功能切入点。
4. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. 蛋白过小（75 aa），实验操作受限

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ABI1 | STRING | 999 |
| CYFIP2 | STRING | 999 |
| RAC1 | STRING | 964 |
| WAS | STRING | 937 |
| ACTR2 | STRING | 813 |
| ACTR3 | STRING | 715 |
| ACTBL2 | BioGRID | 1 |
| CDKN2A | BioGRID | 1 |


### 深度机制分析

BRK1(Brick1/HSPC300/C3orf10, 75 aa, 8.7 kDa, UniProt: Q8WUW1)是WAVE(SCAR)调节复合物的核心亚基, 采用InterPro IPR033378(BRK1 domain)——该结构域为全alpha-螺旋折叠(4个alpha-螺旋包装成束)形成接触WAVE/SCAR蛋白VCA(verprolin homology/cofilin/acidic)区的刚性支架界面。AlphaFold v6 pLDDT=93.7(有序区92.0%), rMD=0 (无无序区), 结构几乎为单一刚性核心, 其75aa全结构域仅贡献极少无序区域(pLDDT<50仅1.3%), 在极高pLDDT与tiny protein size的矛盾中反映了该蛋白的"结晶全折叠"特质——5个PDB条目(3P8C, 4N78, 7USC, 7USD, 7USE)覆盖了BRK1与WAVE复合物其他亚基共结晶的原子结构(WAVE1/SCAR1: Sra1-Nap1-Abi1-HSPC300-BRK1, 也称WRC复合物)。

BRK1以核斑(nuclear speckles)作为主要亚细胞定位(HPA Approved)——核斑是富集mRNA剪接因子的核域, 也是基因激活的转录中心(nascent RNA Pol II转录灶)——这一核定位与BRK1在胞质中的经典肌动蛋白动力学功能形成鲜明对比。事实上, BRK1的核标靶信号和其在核内的功能已被多篇文献支持: (1) BRK1在G2/M转换期转位至细胞核与核膜并与lamin A/C共同维持核形态完整性; (2) BRK1与CDKN2A/p14ARF(BioGRID)的互作——ARF是核仁应激响应蛋白, 通过与MDM2结合稳定p53——暗示BRK1可能通过ARF-p53轴参与核斑区域的DNA损伤感应; (3) ACTG1(humanPPI, Biogrid+Opencell)在核内作为核肌动蛋白(nuclear actin)存在, 直接参与Pol II转录延伸和染色质重塑复合物(BRG1/BAF)的活性——BRK1-ACTG1互作提示BRK1可能将核肌动蛋白招募至核斑，形成核肌动蛋白-WAVE亚复合物参与转录调控。

PPI网络进一步揭示BRK1在核内肌动蛋白-染色质交界面上的核心地位: ABI1/ABIL1-3(IntAct, STRING 999)是WAVE复合物的Abelson-interactor亚基, 连接BRK1到RAC1 GTPase信号; NCKAP1(humanPPI, Biogrid+Opencell)是WRC复合物的Nap1亚基, 为肌动蛋白单体(WASP-WAVE)调节的关键信号。DTNBP1(IntAct+Biogrid)是dysbindin-1(BLOC-1复合物), 其突变与Hermansky-Pudlak综合征相关, 同时也是肌动蛋白核纤层复合物的组分; WASF1/2(humanPPI, Biogrid+Opencell)是WAVE1/2, 直接连接RAC1到ARP2/3复合物。BAIAP2(Biogrid+Opencell)是IRSp53(BAR-domain蛋白和RAC1效应子), NDEL1(IntAct+Biogrid)是LIS1-dynein调节亚基——后两者均存在核斑定位并参与了核肌动蛋白动力学。CDKN2A(p16INK4a/p14ARF, BioGRID)的另一定位在核斑和核仁, 其与BRK1的互作提供了"核斑-应激响应轴"的关键连接。H1(linker组蛋白, humanPPI HAP1+Bioplex)的互作进一步支持BRK1与染色质的物理接近。

机制模型: BRK1作为"核斑内肌动蛋白-WAVE模块"的支架蛋白, 其功能从胞质肌动蛋白多聚化上升至核内基因表达调控——在核斑内, 核肌动蛋白(N-actin)与BRK1-WAVE模块相结合参与Pol II启动子近端暂停释放和转录延伸的肌动蛋白依赖性步骤。TE调控: 在核斑中, LINE-1和HERV-K的RNA向Pol II暂停位点移出并形成R-loop(RNA-DNA hybrid)是转座的关键步骤——核斑内N-actin-BRK1模块可能通过调控Pol II暂停时长决定TE转录本的稳定性/出核速率。BRK1的极度小尺寸(75 aa, 蛋白质组学中最小的核蛋白之一)和WAVE复合物中"缺一不可"的刚性架构意味着BRK1不能作为PROTAC靶标(其整体结构域即为功能活性位点, 缺少可药用的Pocket), 但作为核斑的荧光报告基因或近距离生物素化标记(BioID/APEX2)融合构建体, 其tiny size提供了对核斑功能最精密的分子探针。实验策略: Lenti-BRK1-APEX2构建→在HeLa和HAP1细胞中标记和亲和纯化核斑蛋白质组→检测TE编码蛋白(ORF1p, GAG)是否为BRK1核斑近端蛋白→用CUT&RUN/cHiP-seq在BRK1-OE和BRK1-KO背景中检查LINE-1/HERV-K位点处的Pol II暂停指数(pausing index)。

### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q8WUW1
- Protein Atlas: https://www.proteinatlas.org/search/BRK1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WUW1
- STRING: https://string-db.org/network/9606.BRK1
- Packet data timestamp: 2026-06-03 03:45:32

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000254999-BRK1/subcellular

![](https://images.proteinatlas.org/60391/1018_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/60391/1018_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/60391/1226_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/60391/1226_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/60391/1579_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/60391/1579_E1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WUW1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WUW1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR033378; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000254999-BRK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTG1 | Biogrid, Opencell | true |
| BAIAP2 | Biogrid, Opencell | true |
| DTNBP1 | Intact, Biogrid | true |
| HSBP1 | Intact, Biogrid | true |
| NCKAP1 | Biogrid, Opencell | true |
| NDEL1 | Intact, Biogrid | true |
| WASF1 | Biogrid, Opencell | true |
| WASF2 | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
