---
type: protein-evaluation
gene: "BOLA2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BOLA2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BOLA2 / BOLA2A |
| 蛋白名称 | BolA-like protein 2 |
| 蛋白大小 | 86 aa / 10.1 kDa |
| UniProt ID | Q9H3K6 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:42:38 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | UniProt: Cytoplasm, Nucleus |
| 蛋白大小 | 4/10 | x1 | 4 | 86 aa / 10.1 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=24 篇 (21-40->8) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=92.7 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: 3; Pfam: 1; IPR045115, IPR002634... |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.0 | STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **135.0/180** | |
| **归一化总分 (/1.83)** | | | **73.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 无数据; 额外: 无 | N/A |
| UniProt | Cytoplasm, Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- iron-sulfur cluster assembly complex (GO:1990229)
- nucleus (GO:0005634)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 86 aa，蛋白较小，但仍在可操作范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BOLA2A |

**关键文献**:
1. A Glutaredoxin·BolA Complex Serves as an Iron-Sulfur Cluster Chaperone for the Cytosolic Cluster Assembly Machinery.. *The Journal of biological chemistry*. PMID: 27519415
2. The Human-Specific BOLA2 Duplication Modifies Iron Homeostasis and Anemia Predisposition in Chromosome 16p11.2 Autism Individuals.. *American journal of human genetics*. PMID: 31668704
3. Putative roles of glutaredoxin-BolA holo-heterodimers in plants.. *Plant signaling & behavior*. PMID: 24714563
4. Dissecting the autism-associated 16p11.2 locus identifies multiple drivers in neuroanatomical phenotypes and unveils a male-specific role for the major vault protein.. *Genome biology*. PMID: 37968726
5. A PCBP1-BolA2 chaperone complex delivers iron for cytosolic [2Fe-2S] cluster assembly.. *Nature chemical biology*. PMID: 31406370

**评价**: 较高新颖性，研究尚处早期阶段（PubMed 21-40篇）。新颖性评分 8/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.7 |
| 高置信度残基 (pLDDT>90) 占比 | 82.6% |
| 置信残基 (pLDDT 70-90) 占比 | 14.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 96.6% |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold高质量预测（pLDDT=92.7），预测结构可信。三维结构评分 10/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045115, IPR002634, IPR036065; Pfam: PF01722 |

**染色质调控潜力分析**: 存在 4 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GLRX3 | 0.995 | 0.786 | -- |
| BOLA3 | 0.994 | 0.000 | -- |
| GLRX5 | 0.905 | 0.000 | -- |
| BOLA1 | 0.811 | 0.000 | -- |
| CIAPIN1 | 0.797 | 0.280 | -- |
| ISCU | 0.762 | 0.000 | -- |
| FDX2 | 0.753 | 0.000 | -- |
| NFS1 | 0.737 | 0.000 | -- |
| LYRM4 | 0.709 | 0.000 | -- |
| FXN | 0.707 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IQCB1 | anti tag coimmunoprecipitation | pubmed:21565611|imex:IM-16529 |
| GRXS15 | two hybrid array | pubmed:21798944|imex:IM-16043 |
| GRXS17 | two hybrid array | pubmed:21798944|imex:IM-16043 |
| GRXS14 | two hybrid array | pubmed:21798944|imex:IM-16043 |
| VCAM1 | cross-linking study | imex:IM-17358|pubmed:22623428 |
| ARRB2 | anti tag coimmunoprecipitation | pubmed:17620599 |
| BOLA2B | pull down | pubmed:21712045|imex:IM-17900 |
| SOAT1 | cross-linking study | doi:10.1016/j.cels.2017.10.010|pubmed:29128334|imex:IM-26363 |
| PARK7 | cross-linking study | doi:10.1016/j.cels.2017.10.010|pubmed:29128334|imex:IM-26363 |
| CDK1 | cross-linking study | doi:10.1016/j.cels.2017.10.010|pubmed:29128334|imex:IM-26363 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=92.7 | 单一来源 |
| 定位 | UniProt | Nucleus | 单一来源 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**归一化总分**: 73.8/100

**核心优势**:
1. BOLA2 -- BolA-like protein 2，较高新颖性，研究尚处早期阶段。
2. AlphaFold高质量预测（pLDDT=92.7），结构可信度高。
3. 存在 4 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 核定位信号较弱或存在矛盾（评分 4/10），需IF实验验证
2. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测
3. 蛋白过小（86 aa），实验操作受限

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9H3K6
- Protein Atlas: https://www.proteinatlas.org/search/BOLA2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BOLA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H3K6
- STRING: https://string-db.org/network/9606.BOLA2
- Packet data timestamp: 2026-06-03 03:42:38
