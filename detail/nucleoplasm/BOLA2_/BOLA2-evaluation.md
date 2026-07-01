---
type: protein-evaluation
gene: "BOLA2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, nucleoplasm]
status: shortlisted
---

## BOLA2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / Gene Name | BOLA2 (BolA Family Member 2) |
| 蛋白名称 | BolA-like protein 2 |
| 别名 / Aliases | BOLA2A; BOLA2B (paralog); My016; BolA-like protein 2 |
| 蛋白大小 / Protein Size | 86 aa / 10.1 kDa |
| UniProt ID | Q9H3K6 (BOLA2_HUMAN, Swiss-Prot reviewed) |
| 染色体位置 / Chromosomal Location | 16p11.2 (GRCh38: 29,453,587–29,455,012) |
| 蛋白存在证据 / Protein Evidence | 1: Evidence at protein level (直接蛋白测序, N-acetylmethionine确认) |
| HPA 亚细胞定位 / HPA Subcellular Location | Not available (待细胞分析, Pending cell analysis) |
| GO 细胞组分 / GO Cellular Component | Cytoplasm (IDA, PMID: 22746225); Nucleus (IDA, PMID: 22746225); Cytosol (IBA) |
| 生物学功能 / Biological Function | Fe-S cluster assembly factor; 协助[2Fe-2S] cluster插入胞质蛋白; 与GLRX3和CIAPIN1形成复合体 |
| InterPro 结构域 / InterPro Domains | IPR002634 (BolA蛋白); IPR036065 (BolA-like超家族); IPR045115 (BolA-like protein 2) |
| Pfam 结构域 / Pfam Domains | PF01722 (BolA-like protein) |
| AlphaFold 平均 pLDDT / AF Mean pLDDT | 92.69 (Isoform 1); 73.25 (Isoform 2) |
| PubMed 文献数 / PubMed Articles | 31 (总计); 10 (Fe-S cluster / BOLA2功能方向) |
| 16p11.2 基因座 / Locus | 自闭症相关16p11.2 微缺失/微重复区域; 人类特异性BOLA2 gene duplication |
| 评估日期 / Evaluation Date | 2026-06-28 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 / Nuclear Localization | 5/10 | ×4 | 20.0 | GO: Nucleus (IDA, PMID:22746225); 但同时Cytoplasm (IDA)存在; HPA无IF数据; 蛋白主要功能在胞质 (Fe-S cluster assembly); 核定位信号有实验证据但非核心功能 |
| 蛋白大小 / Protein Size | 10/10 | ×1 | 10.0 | 86 aa, 10.1 kDa; 极小蛋白; 结构解析容易; AlphaFold pLDDT 92.69 (极高置信度); 纯化/表达/结晶均无障碍 |
| 研究新颖性 / Research Novelty | 6/10 | ×5 | 30.0 | PubMed 31篇总量适中; 功能方向明确 (Fe-S cluster); 10篇直接BOLA2生物学; 人类特异性duplication + 自闭症关联有研究价值 |
| 三维结构 / 3D Structure | 9/10 | ×3 | 27.0 | pLDDT 92.69 (极高); 83.7%残基>90; 0%<50; Isoform 1结构置信度极高; 86 aa已完整解析; 无PDB但AlphaFold质量达实验级别 |
| 调控结构域 / Regulatory Domains | 3/10 | ×2 | 6.0 | BolA domain (PF01722): 铁硫簇结合, 无DNA/RNA/chromatin调控域; BOLA2为铁代谢蛋白, 不属于经典核调控蛋白家族 |
| PPI网络 / PPI Network | 7/10 | ×3 | 21.0 | 40+个BioGRID互作; 核心伙伴: ISCU/BOLA3/NFS1 (Fe-S簇); EP300 (histone acetyltransferase); CUL3/E3泛素连接酶; NPM1 (核仁蛋白); MCM2 (DNA复制); LARP7/HEXIM1/MEPCE (7SK snRNP复合体) |
| **加权总分** | | | **114/180** | |
| **归一化总分 (÷1.80)** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| GO Cellular Component | Nucleus (GO:0005634, IDA, PMID: 22746225) | 直接实验证据 |
| GO Cellular Component | Cytoplasm (GO:0005737, IDA, PMID: 22746225) | 直接实验证据 |
| GO Cellular Component | Cytosol (GO:0005829, IBA) | 推断 |
| Human Protein Atlas (IF) | 无数据 (Not available; Pending cell analysis) | 无IF图像 |
| UniProt Subcellular Location | Cytoplasm (SL-0086); Nucleus (SL-0191) | 实验证据 (PMID:22746225) |
| 预测定位 (HPA) | Intracellular | — |

**GO 定位/功能** (精选):
- GO:0005737 C:cytoplasm (IDA, PMID: 22746225)
- GO:0005634 C:nucleus (IDA, PMID: 22746225)
- GO:0005829 C:cytosol (IBA)
- GO:0051537 F:2 iron, 2 sulfur cluster binding (IEA, InterPro)
- GO:0051536 F:iron-sulfur cluster binding (IBA)
- GO:0044571 P:[2Fe-2S] cluster assembly (IDA, PMID: 27519415)
- GO:0045454 P:cell redox homeostasis (IDA)
- GO:0006879 P:intracellular iron ion homeostasis (IDA)
- GO:0016226 P:iron-sulfur cluster assembly (IDA)

**IF 图像**:
BOLA2的HPA细胞免疫荧光数据为"Not available"状态, 亚细胞定位分析标记为"Pending cell analysis"。RNA在HEK293细胞中表达最高(1077.9 nTPM), 但未进行ICC/IF成像。蛋白质在血液中经质谱检测浓度为480 ng/L。

**结论**: BOLA2通过GO IDA实验证据确认为Nucleus + Cytoplasm双定位蛋白(PMID: 22746225)。但蛋白的核心功能(胞质Fe-S cluster assembly)主要在胞质中执行, 核定位的生理意义不明确。HPA无IF数据支撑核定位的细胞类型特异性。UniProt同时注释Cytoplasm和Nucleus但不标注信号肽或核定位信号(NLS)。BOLA2作为86 aa的极小球形蛋白, 可能被动扩散进入核内(分子量10.1 kDa, 低于40 kDa的核孔自由扩散阈值), 因此其核定位可能不是主动核转运的结果。

**评分: 5/10** (GO IDA确认核定位有实验证据 +1; 但核心功能在胞质, 核定位可能是被动扩散, 无HPA IF图像, 无法判断核定位的细胞类型/条件特异性; 分子量低于自由扩散阈值提示需谨慎解释核定位功能意义)。

#### 3.2 蛋白大小评估

86 aa / 10.1 kDa, 属于极小蛋白。远低于300-800 aa的实验室最优操作区间。优势在于: 极高的结构稳定性(AlphaFold pLDDT 92.69, 83.7%残基>90), 易于重组表达和纯化, 结晶和NMR结构解析无障碍。劣势在于: 缺乏大蛋白复杂的多域组织和调控潜力, 86 aa不足以编码多个独立功能域。BolA domain本身仅约80 aa, BOLA2几乎就是"一个结构域本身"。

作为极小的铁硫簇结合蛋白, BOLA2的大小在Fe-S cluster assembly因子中具有典型性(类似ISCU, FXN, GLRX3中的domain)。但若考虑TE调控研究, 86 aa的尺寸意味着它不可能像大型chromatin remodeler(如CHD4)或转录因子那样拥有复杂的DNA/蛋白质互作界面。

**评分: 10/10** (虽然远离300-800 aa的实验最优区间, 但极小蛋白的结构解析优势和无序区域缺失(0% pLDDT<50)使其在结构维度上具有压倒性优势; 大小评估主要侧重实验可行性, BOLA2的纯化/结晶可行性极高)。

#### 3.3 研究现状

| 指标 | 数值 |
|---|---|
| PubMed 总数 (BOLA2) | 31 |
| 直接BOLA2生物学 (Fe-S/铁代谢) | 10 |
| PubMed (BOLA2 + transposon) | 0 |
| 最早发表年份 | 2002 (UniProt first public: 2003-06-16) |
| 核功能/转录调控相关比例 | ~10% (7SK snRNP相关, EP300互作等间接关联) |
| 疾病关联/临床应用方向 | ~30% (16p11.2自闭症、肾透明细胞癌预后、乳腺癌凋亡) |

**主要研究方向**:
- **Fe-S cluster assembly核心功能** (PMID: 27519415, 2016; PMID: 31406370, 2019): BOLA2与GLRX3形成异三聚体(2×BOLA2 + 1×GLRX3), 作为[2Fe-2S] cluster chaperone, 与PCBP1形成chaperone复合体递送铁
- **16p11.2基因剂量与自闭症** (PMID: 31668704, 2019): 人类特异性BOLA2 duplication改变铁稳态和贫血易感性; 16p11.2 copy number variation与自闭症谱系障碍强相关
- **癌症生物标志物** (PMID: 39510574, 2024; PMID: 36017386, 2022; PMID: 41465298, 2025): BOLA家族基因在肾透明细胞癌中作为生存预后标志物; BOLA2在肝细胞癌中的预后价值; BOLA2参与乳腺癌sulfatide-β1 integrin-STAT5凋亡通路
- **铁代谢调控** (PMID: 28615454, 2017): 细胞质铁伴侣蛋白介导哺乳动物细胞质铁辅因子递送

**评价**: BOLA2的文献总量适中(31篇), 略低于100篇的新颖性阈值。功能方向高度明确——核心角色是胞质Fe-S cluster assembly, 这一点在多篇高影响力论文(PMID: 27519415 JBC, PMID: 31406370 Nature Chem Biol)中得到验证。与TE调控相关的文献为0篇。BOLA2的核功能(若存在)在文献中完全未研究——所有功能研究聚焦于胞质铁硫簇代谢。16p11.2 CNV(含BOLA2 duplication)与自闭症的关联提示该蛋白可能影响神经发育, 但该表型可能源于铁稳态改变而非直接核功能。

**评分: 6/10** (31篇文献量适中, 功能方向明确但核心在胞质铁代谢, 无核功能/转录调控文献; 非极度新颖但人类特异性duplication和自闭症关联提供了独特的生物学背景)。

**关键文献**:
1. Frey AG et al. (2016). "A Glutaredoxin-BolA Complex Serves as an Iron-Sulfur Cluster Chaperone for the Cytosolic Cluster Assembly Machinery". *J Biol Chem*, 291(46):24014-24026. PMID: 27519415
2. Patel SJ et al. (2019). "A PCBP1-BolA2 chaperone complex delivers iron for cytosolic [2Fe-2S] cluster assembly". *Nat Chem Biol*, 15(9):872-881. PMID: 31406370
3. Giannuzzi G et al. (2019). "The Human-Specific BOLA2 Duplication Modifies Iron Homeostasis and Anemia Predisposition in Chromosome 16p11.2 Autism Individuals". *Am J Hum Genet*, 105(5):947-958. PMID: 31668704
4. Alissa M et al. (2024). "BOLA family genes are the drivers and potential biomarkers of survival in kidney renal clear cell carcinoma patients". *Saudi Med J*, 45(11):1187-1196. PMID: 39510574
5. Suchanski J et al. (2025). "Sulfatide Acts as a Regulatory Molecule Controlling Beta1 Integrin-STAT5 Signaling and BOLA2-Dependent Apoptotic Pathway in Breast Cancer Cells". *Int J Mol Sci*, 26(24):11221. PMID: 41465298

#### 3.4 三维结构分析

| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT (Isoform 1) | 92.69 |
| pLDDT > 90 (Very High) | 83.7% |
| pLDDT 70–90 (Confident) | 12.8% |
| pLDDT 50–70 (Low) | 3.5% |
| pLDDT < 50 (Very Low) | 0.0% |
| 可用 PDB 条目 | 无 |
| PAE 图像可用性 | 有 (v6) |

**Isoform 2 (58 aa, 截短) 结构指标** (参考):
| 指标 | 数值 |
|---|---|
| 平均 pLDDT | 73.25 |
| pLDDT > 90 | 0.0% |
| pLDDT 70–90 | 63.8% |
| pLDDT < 50 | 3.4% |

**PAE数值分析**:
- Isoform 1 (86 aa): 极小的蛋白尺寸使PAE矩阵的意义不同于大型多域蛋白——86×86的矩阵中, 预期全域低PAE (蛋白为单一折叠单元)
- BolA fold 为 α/β sandwich 结构 (SSF82657), 86 aa在AlphaFold中获得极高的pLDDT (92.69), 表明该fold在进化上高度保守且结构极稳定
- 0%的残基pLDDT<50, 83.7%>90, 说明蛋白几乎全部以高置信度折叠, 无序区域可忽略不计

**评价**: BOLA2 Isoform 1在AlphaFold v6中获得极高置信度——平均pLDDT 92.69, 83.7%残基>90, 0%<50。86 aa的小尺寸使得AlphaFold对其结构的预测接近实验级别精度。BolA fold (α/β sandwich)进化保守, 在细菌中高度保守(BolA/IbaG家族), 在人类中保留完整。Isoform 2 (58 aa截短) pLDDT 73.25, 因过早终止密码子导致C末端缺失, 可能经NMD降解。无PDB实验结构是唯一缺憾, 但由于蛋白极小、pLDDT极高, AlphaFold预测已足够准确用于结构功能推断。**评分: 9/10** (极高pLDDT, 0%无序区域, 结构预测达实验级别精度; -1因无独立PDB实验结构验证, 暂不能得满分)。

#### 3.5 结构域分析

| 来源 | 结构域 |
|---|---|
| UniProt | BolA-like protein 2 (1-86); 属于BolA/IbaG family |
| InterPro | IPR002634 (BolA蛋白); IPR036065 (BolA-like超家族); IPR045115 (BolA-like protein 2) |
| Pfam | PF01722 (BolA-like protein) |
| PANTHER | PTHR12735:SF42 (BOLA-like protein 2); PTHR12735 (BOLA-like protein-related) |
| PIRSF | PIRSF003113 (BolA, stress-induced morphoprotein) |
| CATH/Gene3D | G3DSA:3.30.300.90 (BolA-like) |
| SUPERFAMILY | SSF82657 (BolA-like) |

**TE调控潜力分析**:
BOLA2的BolA domain (PF01722)是一个进化古老的铁硫簇结合域家族, 在原核生物(BolA/IbaG)中高度保守。BolA蛋白家族的核心功能是cell envelope biogenesis、stress response和iron-sulfur cluster homeostasis, 与DNA/RNA/chromatin调控完全无关。

BOLA2不含任何已知的DNA结合域(如zinc finger、helix-turn-helix、homeodomain、winged helix等)、chromatin reader/writer域(如bromodomain、chromodomain、PHD finger、SET domain等)、或转录调控域(如activation domain、repression domain)。PDB和UniProt均未列出任何核酸结合残基或DNA/RNA互作界面。

从结构域角度评估, BOLA2的分子功能与TE调控毫无关联。它是一个纯粹的铁硫簇代谢蛋白, 其保守结构域(BolA)的进化历史可追溯到细菌, 仅与金属离子结合和氧化还原功能相关。有些文献显示BOLA2与7SK snRNP复合体成员(LARP7、HEXIM1、MEPCE)有BioGRID高通量互作, 可能提示间接的核功能关联, 但BolA domain本身不支持任何直接调控功能。

**评分: 3/10** (有明确保守结构域 +1, 多库一致确认 +0.5, 结构域功能明确(铁硫簇结合) +0.5; 但BolA domain与DNA/RNA/chromatin调控完全无关, 不支持TE调控假设; 无法获得染色质/转录调控相关加分; 基线1分 + 域存在 + 功能明确 = 3分)。

#### 3.6 PPI 网络

**核心功能互作** (从本地核PPI数据库和文献):

| Partner | Source | Score/Evidence | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| **Fe-S cluster核心** |
| ISCU | STRING | 764 | Iron-sulfur cluster scaffold | 铁代谢 |
| BOLA3 | STRING | 994 | BolA家族蛋白 (线粒体Fe-S) | 铁代谢 |
| NFS1 | STRING | 739 | Cysteine desulfurase (Fe-S assembly) | 铁代谢 |
| GLRX3 | 文献 | 复合体形成 | Monothiol glutaredoxin (Fe-S chaperone) | 铁代谢 |
| PCBP1 | BioGRID | 1 | Iron chaperone (Fe delivery to BOLA2) | 铁代谢 |
| **核/染色质/转录关联** |
| EP300 | BioGRID | 1 | Histone acetyltransferase (HAT) | 染色质调控 |
| CUL3 | BioGRID | 1 | Cullin-RING E3 ubiquitin ligase | 泛素-蛋白酶体 |
| CUL2 | BioGRID | 1 | Cullin-RING E3 ubiquitin ligase | 泛素-蛋白酶体 |
| NPM1 | BioGRID | 1 | Nucleophosmin (核仁蛋白, histone chaperone) | 核仁/染色质 |
| HIST1H3E | BioGRID | 1 | Histone H3.1 | 染色质 |
| MCM2 | BioGRID | 1 | DNA replication licensing factor | DNA复制 |
| **7SK snRNP 复合体成员** |
| LARP7 | BioGRID | 1 | 7SK snRNP component (P-TEFb regulation) | 转录调控 |
| HEXIM1 | BioGRID | 1 | 7SK snRNP component (P-TEFb inhibitor) | 转录调控 |
| MEPCE | BioGRID | 1 | 7SK snRNA methylphosphate capping enzyme | 转录调控 |
| **剪接/RNA加工** |
| PRPF8 | BioGRID | 1 | U5 snRNP component (spliceosome) | RNA加工 |
| EFTUD2 | BioGRID | 1 | U5 snRNP component (spliceosome) | RNA加工 |
| EIF4A3 | BioGRID | 1 | Exon junction complex (EJC) component | RNA加工 |
| MAGOH | BioGRID | 1 | Exon junction complex (EJC) component | RNA加工 |
| **信号/凋亡** |
| STAT4 | STRING | 750 | STAT transcription factor | 转录调控 |
| XIAP | BioGRID | 1 | X-linked inhibitor of apoptosis | 凋亡 |
| BIRC2/BIRC3/BIRC7 | BioGRID | 1 | IAP family (apoptosis regulation) | 凋亡 |
| PARK7 | BioGRID | 1 | DJ-1 (oxidative stress response) | 氧化应激 |
| CRBN | BioGRID | 1 | Cereblon (E3 ubiquitin ligase component) | 泛素-蛋白酶体 |
| CDK1 | BioGRID | 1 | Cyclin-dependent kinase 1 (cell cycle) | 细胞周期 |

**PPI互证分析**:
- BOLA2的PPI网络呈现明显的功能分层:
  - **核心层**: ISCU/BOLA3/NFS1/GLRX3 — 铁硫簇组装核心, 文献验证与功能完全一致
  - **核/染色质层**: EP300 (HAT), NPM1 (核仁蛋白), HIST1H3E (histone H3.1), MCM2 (DNA复制) — 均为BioGRID高通量互作, 无独立验证, 但多个核蛋白同时出现增加了非随机关联的可能性
  - **7SK snRNP层**: LARP7/HEXIM1/MEPCE — 转录延伸调控复合体, 三个成员同时出现暗示BOLA2可能与7SK RNP存在距离上的关联
  - **剪接/RNA层**: PRPF8/EFTUD2/EIF4A3/MAGOH — spliceosome和EJC成分
- 调控相关比例: 约50% (考虑EP300/NPM1/HIST1H3E/LARP7/HEXIM1等核功能partner)
- 多源验证: ISCU和STAT4有STRING+BioGRID双源; BOLA3在STRING中获得极高分数(994); 但核关联互作均为单一BioGRID高通量记录

**评价**: BOLA2的PPI网络在数量上非常丰富(40+个BioGRID互作), 呈现两种截然不同的功能模式。**胞质核心网络**(ISCU/BOLA3/NFS1/GLRX3/PCBP1)铁硫簇组装功能高度一致, 文献充分验证。**核网络**(EP300/NPM1/HIST1H3E/LARP7/HEXIM1)缺乏任何独立验证, 所有互作均为单一BioGRID高通量检测, 可能反映了核蛋白丰度高导致的pass-by绑定、或BOLA2在核提取过程中与这些蛋白共纯化的假象。7SK snRNP(LARP7/HEXIM1/MEPCE)三个成员的共同出现是唯一值得关注的模式——若BOLA2确与7SK RNP存在低亲和力互作, 理论上可能通过影响P-TEFb介导的转录延伸来间接影响基因组调控(包括TE转录)。但目前证据级别极低。

**评分: 7/10** (PPI数量丰富 +1; 核心铁硫簇网络高度一致+1; 核网络存在有趣的7SK snRNP关联模式 +0.5; 但所有核互作为单一高通量记录, 无独立验证 -0.5; 综合: 5分基线 + 数量(+1) + 核心一致性(+0.5) + 核模式(+0.5) = 7分)。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold | pLDDT 92.69, 极高置信度 | 与BolA域预测一致 (+0.5) |
| 结构域 | UniProt/InterPro/Pfam/PIRSF/PANTHER/CATH/SUPERFAMILY | BolA domain (PF01722), 7库一致 | 多库一致 (+0.5) |
| 域功能一致 | GO + 文献 (Fe-S assembly) | BolA domain功能为铁硫簇结合, 与GO完全吻合 | 一致 (+0.5) |
| 定位互证 | GO (IDA, Nucleus+Cytoplasm) + UniProt | 双定位确认 | 一致 (+0.5) |
| PPI | STRING + BioGRID + 文献 | 胞质Fe-S网络多源验证; 核关联单一高通量 | 部分一致 (+0) |

**互证加分明细**:
- 三维结构互证: AlphaFold极高pLDDT与BolA域结构预测一致 (+0.5)
- 结构域互证: 7个数据库同时确认BolA domain (UniProt/InterPro/Pfam/PIRSF/PANTHER/CATH/SUPERFAMILY) (+0.5)
- 域功能一致: BolA domain (铁硫簇结合) 与 GO Fe-S cluster assembly (IDA) 功能完全吻合 (+0.5)
- 定位互证: UniProt + GO 一致确认Cytoplasm+Nucleus双定位 (+0.5)
- PPI: 胞质核心网络多源一致, 但核网络仅单一高通量源 (+0)
- 进化保守性: BolA domain在细菌到人类高度保守, 人类BOLA2经gene duplication产生两个拷贝(BOLA2A/BOLA2B)

**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: **中低** (2.5/5) —— 作为TE调控候选蛋白存在可能性但证据非常薄弱

**核心优势**:
1. **结构质量极高**: AlphaFold pLDDT 92.69 (83.7%>90, 0%<50), 86 aa极小蛋白, 可进行高精度结构分析和体外实验, 纯化/结晶无障碍
2. **PPI网络丰富**: 40+个BioGRID核互作, 其中7SK snRNP复合体(LARP7/HEXIM1/MEPCE)和EP300/HIST1H3E/NPM1等核调控因子的出现提供了间接核功能假设
3. **人类特异性duplication**: BOLA2在16p11.2经人类特异性gene duplication产生两个活跃拷贝(BOLA2A/BOLA2B), 与自闭症谱系障碍强关联; 人类特异性的基因剂量改变可能影响TE调控(若BOLA2确有核功能)
4. **多数据库高度一致**: 7个结构域数据库一致确认BolA fold, 功能与GO IDA实验证据完全吻合

**核心弱点**:
1. **核心功能与核调控无关**: BolA domain是铁硫簇结合域, BOLA2的生物学功能是胞质Fe-S cluster assembly。所有功能研究均聚焦于此, 没有任何文献研究核功能
2. **核定位可能是被动扩散**: 10.1 kDa的蛋白可自由通过核孔(40 kDa cutoff), 其核内存在可能是物理性的而非功能性的
3. **所有核关联PPI均为单一高通量**: EP300, NPM1, HIST1H3E, LARP7, HEXIM1等核partner均来自单一BioGRID高通量互作(evidence=1), 无重复验证、无复合体形成证据、无功能验证
4. **HPA无IF数据**: 无法确认在哪些细胞类型、何种条件下BOLA2定位于核内; Nucleoplasm定位无ICC/IF图像支持
5. **无DNA/RNA/chromatin结合域**: BOLA2没有已知的核酸互作界面, 若真有核功能, 其机制必须通过蛋白质-蛋白质互作(而不直接结合DNA)实现

**TE调控相关性评估**:
BOLA2直接参与TE调控的可能性非常低。其核心功能(铁硫簇组装)与基因组调控无明显交集。然而, 以下间接线索值得注意:

1. **铁硫簇与基因组稳定性**: Fe-S cluster proteins在DNA复制(PrimPol, DNA polymerase)、DNA repair(Glycosylases, XPD helicase)和telomere maintenance中具有关键作用。BOLA2作为Fe-S cluster assembly/chaperone因子, 若其功能延伸至核内, 理论上可能通过影响核内Fe-S蛋白成熟来间接影响基因组稳定性。但此推断完全未经实验验证。

2. **7SK snRNP关联**: BOLA2与7SK snRNP复合体成员(LARP7/HEXIM1/MEPCE)存在BioGRID高通量互作。7SK snRNP调控P-TEFb(CDK9/Cyclin T1)活性, 而P-TEFb是RNA Pol II转录延伸的关键因子。若BOLA2与7SK RNP存在真实的功能性关联, 理论上可通过调节Pol II延伸率影响全基因组转录水平, 包括TE区域的转录。但三个BioGRID互作均为单一高通量记录, 证据级别极低。

3. **EP300互作**: EP300 (p300)是histone acetyltransferase, 在enhancer activation和chromatin decompaction中起核心作用。BOLA2与EP300的互作(若真实)暗示可能通过影响组蛋白乙酰化来调控chromatin状态。但同样:单一BioGRID记录, 无验证。

**诚实地评估**: BOLA2是一个优雅的铁硫簇代谢蛋白, 其分子功能清晰、结构优质。但它不是TE调控蛋白——其BolA domain不支持DNA/RNA/chromatin binding, 核定位可能是被动扩散的结果, 所有核关联PPI证据都微弱。BOLA2在16p11.2自闭症基因座的duplication更可能与铁稳态和氧化应激的改变有关, 而非直接的基因组调控。

如果希望寻找一个TE调控蛋白, BOLA2不是合适的选择。如果对铁代谢与chromatin biology的交叉感兴趣(例如Fe-S cluster proteins在chromatin remodeling和DNA repair中的作用), BOLA2可能是一个有价值的工具蛋白——研究Fe-S cluster assembly如何间接影响核功能——但这与TE regulation的关联需要大量额外的假设。

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9H3K6
- AlphaFold (Isoform 1): https://alphafold.ebi.ac.uk/entry/Q9H3K6
- AlphaFold (Isoform 2): https://alphafold.ebi.ac.uk/entry/Q9H3K6-2
- HPA (BOLA2): https://www.proteinatlas.org/ENSG00000183336-BOLA2
- HPA Subcellular: https://www.proteinatlas.org/ENSG00000183336-BOLA2/subcellular
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q9H3K6/
- Pfam: https://www.ebi.ac.uk/interpro/entry/pfam/PF01722/
- PubMed Search: https://pubmed.ncbi.nlm.nih.gov/?term=BOLA2
- STRING: https://string-db.org (API, species=9606)
- BioGRID: https://thebiogrid.org (BOLA2 interactors)
- NCBI Gene: https://www.ncbi.nlm.nih.gov/gene/552900 (BOLA2A) / 654483 (BOLA2B)
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=BOLA2

### 6. 补充说明

#### PPI 网络（本地核PPI数据）

BOLA2在本地核PPI数据库中显示丰富的互作网络:

**STRING 预测互作** (BOLA2A, 去BOLA2B):

| Partner | Score | 功能类别 |
|---|---|---|
| ISCU | 764 | Iron-sulfur cluster scaffold |
| STAT4 | 750 | STAT transcription factor |
| BOLA3 | 994 | BolA family (mitochondrial Fe-S) |
| NFS1 | 739 | Cysteine desulfurase |

**BioGRID 实验互作** (BOLA2A, 精选):

| Partner | Function |
|---|---|
| CUL3 | Cullin-RING E3 ligase |
| CUL2 | Cullin-RING E3 ligase |
| MAGOH | Exon junction complex |
| EIF4A3 | Exon junction complex |
| PAN2 | Deadenylation nuclease |
| NPM1 | Nucleophosmin (nucleolar, histone chaperone) |
| HIST1H3E | Histone H3.1 |
| MCM2 | DNA replication licensing |
| CRBN | Cereblon (E3 ligase) |
| CDK1 | Cyclin-dependent kinase 1 |
| COX15 | Cytochrome c oxidase assembly |
| PARK7 | DJ-1 (oxidative stress) |
| PCBP1 | Iron chaperone |
| UBE2M | NEDD8-conjugating enzyme |
| PRPF8 | U5 snRNP (spliceosome) |
| EFTUD2 | U5 snRNP (spliceosome) |
| PIH1D1 | R2TP complex (Hsp90 co-chaperone) |
| HEXIM1 | 7SK snRNP (P-TEFb inhibitor) |
| MEPCE | 7SK snRNA capping |
| LARP7 | 7SK snRNP scaffold |
| WWP2 | E3 ubiquitin ligase |
| EP300 | Histone acetyltransferase (p300) |
| ZNF76 | Zinc finger transcription factor |
| XIAP | X-linked IAP |
| BIRC2/BIRC3/BIRC7 | IAP family |
| ID3 | Inhibitor of DNA binding (HLH TF) |
| HDX | Highly divergent homeobox |
| CGGBP1 | CGG triplet repeat binding protein |
| CCDC138 | Coiled-coil domain (unknown) |
| WDYHV1 | N-terminal glutamine amidase |

#### PAE图像 (Isoform 1)

![](https://alphafold.ebi.ac.uk/files/AF-Q9H3K6-F1-predicted_aligned_error_v6.png)

**PAE图像说明**: 86 aa的极小蛋白, PAE矩阵(86×86)整体呈现全域低predicted aligned error, 与极高的pLDDT (92.69)一致。蛋白为单一折叠单元, 无独立的折叠域间低PAE信号(因蛋白仅一个domain)。PAE图证实BolA fold在AlphaFold v6模型下被预测为高度刚性的紧凑结构。

#### Isoform 2 信息

BOLA2存在两个isoform:
- **Isoform 1 (Q9H3K6-1)**: 86 aa, 完整的BolA domain, 主要功能形式
- **Isoform 2 (Q9H3K6-2)**: 58 aa, 位置55-58替换为FCTE, 位置59-86缺失; 因提前终止密码子可能导致nonsense-mediated mRNA decay, 生理水平极低; AlphaFold pLDDT 73.25

#### 人类特异性Gene Duplication

BOLA2位于16p11.2重复区: BOLA2A (ENSG00000183336)和BOLA2B (ENSG00000274770)几乎完全相同的两个拷贝, 编码identical蛋白。人类特异性duplication可能在~282 kya发生, 导致人类比其他灵长类多一个BOLA2拷贝。16p11.2微缺失(含BOLA2A/B)和微重复(增加BOLA2拷贝)均与自闭症谱系障碍、智力障碍和肥胖风险相关。BOLA2基因剂量改变影响铁稳态(PMID: 31668704)。

#### HPA IF 图像状态

BOLA2目前无HPA免疫荧光图像。亚细胞定位状态为"Not available", 可靠性评分"Pending cell analysis"。RNA在HEK293中高表达(1077.9 nTPM), 但ICC/IF未进行。蛋白质质谱在血液中检测浓度为480 ng/L。抗体信息不详。

#### TE调控最终评估

BOLA2的分子功能、结构域组成和已知生物学角色不支持TE调控假设。其核定位虽经GO IDA实验确认, 但可能仅反映被动扩散(10.1 kDa)。所有关联核调控蛋白的PPI信号(EP300/NPM1/HIST1H3E/7SK snRNP)均为单一高通量记录, 证据级别不足以建立功能联系。BOLA2更适合作为铁代谢研究而非TE调控研究的对象。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| IREB2 | STRING | 714 |
| PRKCQ | STRING | 922 |
| BOLA2B | STRING | 535 |
| ACO1 | STRING | 402 |
| ISCU | STRING | 448 |
| BOLA2 | STRING | 543 |
| BOLA3 | STRING | 450 |
| GLRX2 | STRING | 484 |
| GLRX3 | STRING | 838 |
| BOLA1 | STRING | 400 |
| NDOR1 | STRING | 594 |
| NFS1 | STRING | 450 |
| GLRX | STRING | 472 |
| CIAPIN1 | STRING | 715 |

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| IREB2 | STRING | 714 |
| PRKCQ | STRING | 922 |
| BOLA2B | STRING | 535 |
| ACO1 | STRING | 402 |
| ISCU | STRING | 448 |
| BOLA2 | STRING | 543 |
| BOLA3 | STRING | 450 |
| GLRX2 | STRING | 484 |
| GLRX3 | STRING | 838 |
| BOLA1 | STRING | 400 |
| NDOR1 | STRING | 594 |
| NFS1 | STRING | 450 |
| GLRX | STRING | 472 |
| CIAPIN1 | STRING | 715 |

