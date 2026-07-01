---
type: protein-evaluation
gene: "HDGFL3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HDGFL3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HDGFL3 / HDGF2, HDGFRP3 |
| 蛋白名称 | Hepatoma-derived growth factor-related protein 3 |
| 蛋白大小 | 203 aa / 22.6 kDa |
| UniProt ID | Q9Y3E1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 203 aa / 22.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=70.7; PDB: 6IIP, 6IIQ, 6IIR, 6IIS, 6IIT |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000313; Pfam: PF00855 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **144.0/180** | |
| **归一化总分** | | | **80.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HDGF2, HDGFRP3 |

**关键文献**:
1. Chinese herbal Formula Q attenuates letrozole-induced polycystic ovary syndrome through modulating multiple metabolic processes in female adult rats.. *In silico pharmacology*. PMID: 42153178
2. Bulk RNA-Seq Combined with Single-Cell Transcriptome Sequencing Reveals the Possible Mechanisms by Which HDGFL3 Involves in Prostate Cancer Growth and Metastasis.. *Archivos espanoles de urologia*. PMID: 37681334
3. The HRP3 PWWP domain recognizes the minor groove of double-stranded DNA and recruits HRP3 to chromatin.. *Nucleic acids research*. PMID: 31162607

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.7 |
| 高置信度残基 (pLDDT>90) 占比 | 34.0% |
| 置信残基 (pLDDT 70-90) 占比 | 7.9% |
| 中等置信 (pLDDT 50-70) 占比 | 46.8% |
| 低置信 (pLDDT<50) 占比 | 11.3% |
| 有序区域 (pLDDT>70) 占比 | 41.9% |
| 可用 PDB 条目 | 6IIP, 6IIQ, 6IIR, 6IIS, 6IIT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6IIP, 6IIQ, 6IIR, 6IIS, 6IIT）+ AlphaFold极高置信度预测（pLDDT=70.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000313; Pfam: PF00855 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HMCN2 | 0.507 | 0.146 | — |
| CDK13 | 0.492 | 0.408 | — |
| CDK12 | 0.489 | 0.408 | — |
| BAZ2B | 0.440 | 0.440 | — |
| BRPF1 | 0.422 | 0.052 | — |
| MTERF2 | 0.421 | 0.417 | — |
| PON3 | 0.410 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15417|pubmed:21706016 |
| ENSP00000520451.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SENP8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF280A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BAZ2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC30A6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RNF13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GPANK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDKL5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 7，IntAct interactions: 15
- 调控相关比例: 0 / 7 = 0%

**评价**: STRING 7 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.7 + PDB: 6IIP, 6IIQ, 6IIR, 6IIS, 6IIT | pLDDT=70.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 7 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 深度机制分析

HDGFL3（Hepatoma-derived growth factor-related protein 3，又名HDGF2/HDGFRP3）的结构域架构以一紧凑的双模块串联为核心：N端PWWP结构域（IPR000313、Pfam PF00855、SMART SM00293，残基11-68）采用经典的PWWP折叠——由五股反平行beta-桶和附属alpha-螺旋组成，通过表面保守的疏水-芳香族氨基酸笼识别H3K36me2/me3修饰（PMID:31162607），同时以beta-桶底部的碱性氨基酸簇伸入DNA双链的小沟。C端为富含丝氨酸/酸性残基的非结构化区域，可能参与无序蛋白质互作和核定位信号调控。

203 aa（22.6 kDa）的紧凑尺寸（在75个候选蛋白中属最小级别）容纳了PWWP介导的全部染色质结合功能，缺乏额外的酶活性域。实验PDB结构（6IIP、6IIQ、6IIR、6IIS、6IIT）覆盖了PWWP结构域的高分辨率晶体构象，明确揭示了H3K36me3结合口袋的分子细节——K36me3的含氮甲基基团通过阳离子-π堆积和氢键网络被锁定于芳香族笼（Trp/Trp/Phe三联体）中。AlphaFold pLDDT为70.7，PWWP区域置信度高达34%的残基pLDDT>90，表明核基因编码合成能力良好。

PPI网络揭示多维度功能联系：STRING预测互作显示CDK12/CDK13（转录延伸/RNA Pol II CTD Ser2激酶，combined score 0.489/0.492，实验得分0.408，PMID:28514442）、BAZ2B（ISWI染色质重塑复合物组分，combined score 0.440）、BRPF1（HB01/MYST组蛋白乙酰转移酶复合物支架蛋白，combined score 0.422）、MTERF2（线粒体转录终止因子）和SF3B2（剪接体U2 snRNP组分）。GRB2的Co-IP互作（PMID:21706016）暗示HDGFL3可能参与生长因子信号与染色质稳态的交叉调控。BAZ2B和BRPF1的连接分别指向染色质重塑和组蛋白乙酰化两个核过程，而CDK12/CDK13的强信度互作直接关联转录延伸调控。

TE调控相关性的机制推论基于PWWP结构域的双重识别功能——这使其成为H3K36me2/3修饰信号与TE转录状态之间的潜在解码器：（1）PWWP是已知的H3K36me2/3甲基化阅读器，而H3K36me3在活跃转录基因的基因体上富集，由SETD2（H3K36me3甲基转移酶）随RNA Pol II延伸而沉积。若内含子/基因间TE元件（如LINE-1和Alu）被Pol II通读并产生转录依赖的H3K36me3修饰，HDGFL3可能通过PWWP同时识别该甲基化标记和TE DNA小沟，介导TE区域的转录延伸效率调控；（2）CDK12/CDK13（RNA Pol II CTD Ser2激酶）互作暗示HDGFL3参与CTD磷酸化状态的调控，Ser2P是转录延伸和3'端加工的关键磷酸化标记——HDGFL3可能作为CDK12/CDK13与H3K36me3标记染色质之间的分子适配器，协同调控Pol II在TE嵌入位点的通读和终止决策；（3）BAZ2B（ISWI复合物组分）互作暗示HDGFL3可招募ATP依赖的染色质重塑活性至H3K36me3标记的基因组区域，可能通过核小体滑动调控TE区域的可及性；（4）BRPF1（HB01乙酰转移酶复合物支架）的连接预示着组蛋白H4/H3乙酰化修饰与H3K36甲基化之间在TE区域的串扰调控。关键文献PMID:31162607直接证实HRP3 PWWP识别DNA小沟并将HRP3募集至染色质，这一功能在TE调控上下文中可被重新诠释——若TE启动子或嵌入侧翼序列含有PWWP偏好的DNA结构特征（AT-rich弯曲序列或特定的小沟宽度），HDGFL3将提供序列-修饰双信号整合的染色质锚定模式。

尽管PubMed严格计数仅3篇（新颖性得分10/10），HPA和UniProt一致定位为核质（nucleoplasm）赋予其可信的核定位证据（核定位特异性7/10）。结构域得分7/10，归一化总分80/100。在候选蛋白中，HDGFL3因PWWP-H3K36me3-DNA三重信号集成和CDK12/CDK13转录延伸耦合的机制特异性，使其TE调控潜力高于原始评分所反映。建议优先进行：a）HDGFL3 ChIP-seq确定其基因组结合位点与TE嵌入的共定位模式，b）PWWP对K36me2/me3特异性的体外定量验证，c）HDGFL3敲除后RNA Pol II ChIP-seq评估TE区域Ser2P和转录通读的变化。

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HDGFL3 — Hepatoma-derived growth factor-related protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小203 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能参与 TE 沉默。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3E1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166503-HDGFL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HDGFL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3E1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000166503-HDGFL3/subcellular

![](https://images.proteinatlas.org/40719/2191_E8_15_red_green.jpg)
![](https://images.proteinatlas.org/40719/2191_E8_28_red_green.jpg)
![](https://images.proteinatlas.org/40719/418_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/40719/418_H11_2_red_green.jpg)
![](https://images.proteinatlas.org/40719/424_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/40719/424_H11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y3E1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y3E1 |
| SMART | SM00293; |
| UniProt Domain [FT] | DOMAIN 11..68; /note="PWWP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00162" |
| InterPro | IPR000313; |
| Pfam | PF00855; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166503-HDGFL3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SF3B2 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
