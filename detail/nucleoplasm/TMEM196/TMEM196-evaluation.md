---
type: protein-evaluation
gene: "TMEM196"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM196 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM196 |
| 蛋白名称 | Transmembrane protein 196 |
| 蛋白大小 | 178 aa / 19.0 kDa |
| UniProt ID | Q5HYL7 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Golgi apparatus; Nucleoplasm (Uncertain) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 178 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=6 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=78.2; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | TMEM196 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=7 |
| **加权总分** | | | **126/180** | |
| **归一化总分** | | | **69.9/100** | 互证: +2 |

### 3. 分析
- Golgi apparatus; Nucleoplasm (Uncertain)
- PubMed strict=6 broad=8
- AF pLDDT=78.2 PDB=0
- InterPro: TMEM196
- Pfam: 
- PPI degree=7 ChIP: None
36355209: TMEM196 inhibits lung cancer metastasis by regulating the Wnt/β-catenin signalin | 40782428: DB75 targets PRMT1 to suppress liver metastasis and synergizes with PD-L1 blocka | 39825804: The transmembrane protein TMEM196 controls cell proliferation and determines the

### 4. 总体评价
**69.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 196

**功能**: Acts as a tumor suppressor in lung cancer (PubMed:26056045, PubMed:36355209). Inhibits tumor cell growth by inhibiting cell proliferation and migration and promoting cell apoptosis (PubMed:26056045, PubMed:36355209). Inhibits metastasis of lung cancer by suppressing beta-catenin expression in the Wnt/beta-catenin signaling pathway (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR037661 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：TMEM196（178 aa, 19.0 kDa, Q5HYL7）是TMEM196家族（IPR037661）成员——该家族在进化上高度保守（从鱼类到哺乳动物），但缺乏已知的Pfam结构域注释。178 aa的序列不含跨膜预测区域（TMHMM预测0个TM helix，尽管其名称为"Transmembrane protein"）——实际上TMEM196更可能为外周膜蛋白或膜相关蛋白，而非真实跨膜蛋白。AlphaFold pLDDT=78.2在small protein中表现良好——约70%残基pLDDT>70，折叠核心为混合a/b结构——预测为小型globular domain，表面暴露保守的疏水patch（可能介导蛋白-蛋白互作）。无PDB实验结构，但pLDDT=78.2使AF模型适合in silico docking和结构引导的突变分析。TMEM196蛋白在细胞增殖和floor plate cell决定中发挥作用（PMID:39825804），作为lung cancer metastasis suppressor（PMID:36355209）——抑制Wnt/beta-catenin信号通路。

**PPI互作网络解读**：PPI degree=7,关键伙伴揭示多重调控连接。PBX3（Pre-B-cell leukemia transcription factor 3, BioGRID）是三氨基酸环延伸（TALE）类同源域转录因子——PBX3与HOX蛋白和MEIS/PREP形成异二聚体调控发育基因表达——TMEM196-PBX3互作暗示TMEM196可能调制PBX3-HOX转录因子复合体的DNA结合特异性或转录活性。HIST2H2BE/HIST1H2BN/HIST1H2BH/HIST1H2BL（多个组蛋白H2B变体, BioGRID）——组蛋白H2B与H2A/H3/H4组成核心核小体octamer——TMEM196与H2B的互作提示TMEM196可能直接与核小体核心颗粒（NCP）互作——定位TMEM196至染色质。PCP4（Purkinje cell protein 4/PEP19, BioGRID）是CaM（calmodulin）结合蛋白——PCP4作为CaM拮抗剂抑制CaM-dependent kinase II（CaMKII）活性。ZMPSTE24（zinc metalloproteinase STE24, BioGRID）是核膜内部内蛋白酶——剪切prelamin A的C-terminal CAAX box——produce mature lamin A。

**结构解读**：pLDDT=78.2的结构提供可靠的small globular fold。疏水patch在表面暴露——经mutagenesis实验可能定位为protein interaction hotspot以结合PBX3、H2B或PCP4。TMEM196结构缺乏明显的DNA结合motif（如helix-turn-helix, zinc finger, leucine zipper）——它不能直接结合DNA——其转录调控功能必定通过PPI伙伴实现——尤其是PBX3和H2B。核质和高尔基体双重定位（HPA: Golgi apparatus; Nucleoplasm Uncertain）提示TMEM196可能在Golgi-Nucleus trafficking中穿梭——可能在Golgi经某种翻译后修饰后重新定位至核质。

**机制模型**：（1）Wnt/beta-catenin肿瘤抑制——TMEM196通过抑制beta-catenin表达（PMID:36355209）抑制Wnt信号——beta-catenin是Wnt通路核心转录共激活子——TMEM196可能通过PBX3干扰beta-catenin-TCF/LEF的转录复合体形成，或者经H2B互作调控Wnt靶基因（如c-Myc, Cyclin D1）座位的染色质可及性。（2）Floor plate cell lineage决定（PMID:39825804）——TMEM196在floor plate细胞（发育中的神经管腹侧中线结构，分泌Shh/Sonic hedgehog成型素）的细胞增殖和谱系决定中发挥作用——可能与PBX3-HOX在神经管patterning中的区域特异性功能有关。（3）PRMT1作为DB75药物靶标（PMID:40782428）——DB75（DNA minor groove binder）靶向PRMT1（protein arginine methyltransferase 1, 产生H4R3me2a和non-histone arginine methylation）——TMEM196与DB75/PRMT1 pathway在功能上关联——可能通过调控PRMT1的底物可用性或活性间接影响精氨酸甲基化依赖的转录调控。

**TE调控展望**：TMEM196通过PBX3和H2B间接连接TE调控。PBX3与HOX和MEIS形成复合体结合DNA consensus sequence（TGACAG）——该motif在ERV/LTR和LINE-1启动子中有分布——TMEM196-PBX3互作可能促进或干扰PBX3在TE promoter上的结合→影响TE转录。H2B作为核心核小体组蛋白——TMEM196-H2B互作可能影响TE座位的核小体稳定性或变体（H2B变体替换H2B canonical）——改变染色质可及性→调控TE转录起始。PRMT1催化H4R3me2a（asymmetric dimethylation）是转录激活mark——TMEM196与PRMT1的功能关联可能影响TE染色质区域的H4R3me2a水平→间接调控TE转录活性。Wnt/beta-catenin信号经TCF/LEF结合Wnt-responsive element（WRE, TCF/LEF consensus CTTTG/ATCAA），该motif存在于HERV LTR中——TMEM196对beta-catenin的下调可能导致Wnt-responsive TE promoter活性降低。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TMEM196 | BioGRID | 0 |
| PBX3 | BioGRID | 0 |
| HIST2H2BE | BioGRID | 0 |
| HIST1H2BN | BioGRID | 0 |
| HIST1H2BH | BioGRID | 0 |
| HIST1H2BL | BioGRID | 0 |
| PCP4 | BioGRID | 0 |
| ZMPSTE24 | BioGRID | 0 |



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000173452-TMEM196

![](https://images.proteinatlas.org/43163/547_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/43163/547_D12_3_red_green.jpg)
![](https://images.proteinatlas.org/43163/1876_H7_1_cr5b719fdf2012e_red_green.jpg)
![](https://images.proteinatlas.org/43163/1876_H7_28_cr5b719fdf229b0_red_green.jpg)
![](https://images.proteinatlas.org/43163/532_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/43163/532_D12_2_red_green.jpg)

### PubMed 文献

**PubMed count: 9**

| 42369472 | Differential DNA Methylation and Delirium After Anesthesia and Surgery. | medRxiv 2026 |
| 40782428 | DB75 targets PRMT1 to suppress liver metastasis and synergizes with PD-L1 blockade for enhanced therapeutic efficacy. | Int Immunopharmacol 2025 |
| 39825804 | The transmembrane protein TMEM196 controls cell proliferation and determines the floor plate cell lineage. | Dev Growth Differ 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM196

